'use client';

import React, { useState, useEffect, useRef } from 'react';
import toast, { Toaster } from 'react-hot-toast';

import Layout from '@/components/Layout';
import { useTheme } from '@/contexts/ThemeContext';
import HftDashboard from '@/components/hft/HftDashboard';
import HftPortfolio from '@/components/hft/HftPortfolio';
import HftLoadingOverlay from '@/components/hft/HftLoadingOverlay';
import HftSettingsModal from '@/components/hft/HftSettingsModal';
import { hftApiService, formatCurrency, formatPercentage, createBotStream } from '@/services/hftApiService';
import { userAPI } from '@/services/api';
import type { HftBotData, HftTradingMode } from '@/types/hft';

import { CheckCircle2, AlertCircle, RefreshCw, Play, Square, LayoutDashboard, Briefcase, MessageCircle, Loader2 } from 'lucide-react';


export default function HftPage() {
    const { theme } = useTheme();
    const isLight = theme === 'light';
    const isSpace = theme === 'space';

    const [activeTab, setActiveTab] = useState<'dashboard' | 'portfolio' | 'activity' | 'watchlist'>('dashboard');
    const [botData, setBotData] = useState<HftBotData>({
        portfolio: {
            totalValue: 0,
            cash: 0,
            holdings: {},
            tradeLog: [],
            startingBalance: 0
        },
        config: {
            mode: 'paper',
            tickers: [],
            riskLevel: 'MEDIUM',
            maxAllocation: 0.25
        },
        isRunning: false,
    });

    const [loading, setLoading] = useState(false);
    const [showSettings, setShowSettings] = useState(false);
    const [liveStatus, setLiveStatus] = useState<any>(null);
    const [connected, setConnected] = useState(false);
    /** Incremented on Start Bot so analysis panels remount and never show cached/previous output. */
    const [botRunKey, setBotRunKey] = useState(0);
    const [globalBotStatus, setGlobalBotStatus] = useState<'IDLE' | 'INITIALIZING' | 'READY' | 'ERROR' | 'STOPPED'>('IDLE');

    const botStatusSeqRef = useRef(0);
    const fastPollRef = useRef<ReturnType<typeof setInterval> | null>(null);
    const actionInFlightRef = useRef(false);

    // ADD THIS BLOCK HERE — new debug logger
    useEffect(() => {
        console.log('[STATE]', { isRunning: botData.isRunning, globalBotStatus, loading });
    }, [botData.isRunning, globalBotStatus, loading]);

    // Poll for bot status separately. Guard against overlapping/stale responses.
    useEffect(() => {
    let consecutiveFailures = 0;

    const checkStatus = async () => {
        if (fastPollRef.current) return; // NEW: fast-poll owns status right after Start
        const seq = ++botStatusSeqRef.current;
        try {
            const res = await hftApiService.getBotStatus();
            if (seq !== botStatusSeqRef.current) return; // ignore stale
            setGlobalBotStatus(res.status);
            setBotData(prev => ({ ...prev, isRunning: res.status !== 'STOPPED' }));
            consecutiveFailures = 0;
        } catch {
            if (seq !== botStatusSeqRef.current) return; // ignore stale
            consecutiveFailures++;
            if (consecutiveFailures >= 3) {
                setGlobalBotStatus(prev => (prev === 'INITIALIZING' ? 'READY' : prev));
            }
        }
    };

        checkStatus();
        const interval = setInterval(checkStatus, 30000); // 30 s
        return () => clearInterval(interval);
    }, []);


    // SSE stream: connect once and keep alive; also do an initial REST load
    useEffect(() => {
        initializeApp();

        const stopStream = createBotStream(
            (_level, _message) => { /* logs no longer shown in UI */ },
            (payload) => {
                // Live bot data snapshot from SSE — never overwrite non-zero cached values with 0
                setConnected(true);
                setBotData(prev => {
                    const prevHoldings = prev.portfolio.holdings || {};
                    const newHoldings = payload.holdings && Object.keys(payload.holdings).length > 0
                        ? payload.holdings
                        : prevHoldings;

                    // Compute totalValue from holdings + cash as a safety net when backend sends 0
                    const rawCash = (payload.cash != null && payload.cash > 0) ? payload.cash : prev.portfolio.cash;
                    const rawTotal = (payload.totalValue != null && payload.totalValue > 0) ? payload.totalValue : prev.portfolio.totalValue;
                    // If still 0 but holdings exist, derive it
                    const holdingsMarketValue = Object.values(newHoldings).reduce((sum: number, h: any) => {
                        const price = h.currentPrice || h.avgPrice || 0;
                        const qty = h.quantity || h.qty || 0;
                        return sum + price * qty;
                    }, 0);
                    const derivedTotal = rawTotal > 0 ? rawTotal : (rawCash + holdingsMarketValue) || prev.portfolio.totalValue;

                    return {
                        ...prev,
                        isRunning: prev.isRunning,
                        portfolio: {
                            ...prev.portfolio,
                            cash: rawCash,
                            totalValue: derivedTotal,
                            unrealizedPnL: payload.unrealizedPnL ?? prev.portfolio.unrealizedPnL,
                            realizedPnL: payload.realizedPnL ?? prev.portfolio.realizedPnL,
                            holdings: newHoldings,
                            investedValue: payload.investedValue ?? prev.portfolio.investedValue,
                            todayGain: payload.todayGain ?? prev.portfolio.todayGain,
                            portfolioHistory: (payload.portfolioHistory && payload.portfolioHistory.length > 0)
                                ? payload.portfolioHistory
                                : prev.portfolio.portfolioHistory,
                        },
                        analysis: payload.analysis ?? prev.analysis,
                    };
                });
            },
            () => setConnected(true),
            // Bot cycle started
            (data) => {
                console.log('🔄 Bot cycle started:', data);
                toast.success(data.message || 'Bot started analyzing watchlist stocks');
            },
            // Ticker analysis complete
            (data) => {
                console.log(`✅ ${data.symbol} analysis complete (${data.completed}/${data.total})`);
                // Optional: show progress toast or update UI
            },
            // Bot cycle complete — one analysis pass finished, more may follow.
            // Don't assume this means the bot stopped. getBotStatus() only
            // returns UI phase (status), not is_running — refreshData() below
            // pulls the real isRunning flag from /bot-data.
            async (data) => {
                console.log('🔁 Analysis cycle complete:', data);

                try {
                    const res = await hftApiService.getBotStatus();
                    setGlobalBotStatus(res.status);
                } catch (err) {
                    console.error('Error fetching bot status after cycle complete:', err);
                }

                try {
                    await refreshData(); // this updates isRunning via getBotData()
                } catch (err) {
                    console.error('Error refreshing data after cycle complete:', err);
                }

                toast.success(data.message || 'Analysis cycle complete', {
                    duration: 4000,
                    icon: '🔁'
                });
            },
        );

        const interval = setInterval(refreshData, 60000);
        return () => {
            stopStream();
            clearInterval(interval);
        };
    }, []);

    const initializeApp = async () => {
        try {
            setLoading(true);
            await loadDataFromBackend();
            setConnected(true);
        } catch (error) {
            console.error('Error initializing app:', error);
            toast.error('Failed to initialize application');
            setConnected(false);
        } finally {
            setLoading(false);
        }
    };

    const botDataSeqRef = useRef(0);

    const loadDataFromBackend = async () => {
    const seq = ++botDataSeqRef.current;
    try {
        const data = await hftApiService.getBotData();
        if (seq !== botDataSeqRef.current) return; // NEW: discard stale response

        const backendMode: HftTradingMode = data?.config?.mode === 'live' ? 'live' : 'paper';
        let watchlistTickers: string[] = [];
        try {
            watchlistTickers = await hftApiService.getWatchlist();
        } catch (watchlistErr) {
            watchlistTickers = data?.config?.tickers || [];
        }
        if (seq !== botDataSeqRef.current) return; // NEW: re-check after the second await

        setBotData(prev => ({
            ...prev,
            ...data,
            isRunning: typeof data?.isRunning === 'boolean' ? data.isRunning : prev.isRunning,
            config: {
                ...prev.config,
                ...data.config,
                mode: backendMode,
                tickers: watchlistTickers
            }
        }));
        setConnected(true);
        if (backendMode === 'live') {
            await loadLiveStatus();
        }
    } catch (error: any) {
        if (seq !== botDataSeqRef.current) return; // NEW: discard stale errors too
        const isTimeout = error?.message?.includes('timeout') || error?.code === 'ECONNABORTED';
        const isNetworkError = error?.message === 'Network Error' || error?.code === 'ERR_NETWORK';
        if (isNetworkError && !botData.isRunning) {
            setConnected(false);
        }
    }
};

    const loadLiveStatus = async (mode: HftTradingMode = tradingMode) => {
        if (mode !== 'live') {
            setLiveStatus(null);
            return;
        }
        try {
            const status = await hftApiService.getLiveStatus();
            setLiveStatus(status);
        } catch (error) {
            console.error('Error loading live status:', error);
        }
    };

    const refreshData = async () => {
        try {
            await loadDataFromBackend();
            if (tradingMode === 'live') {
                await loadLiveStatus('live');
                try {
                    await hftApiService.syncLivePortfolio();
                } catch { /* optional */ }
            } else {
                setLiveStatus(null);
            }
        } catch (error) {
            console.error('Error refreshing data:', error);
        }
    };



    const handleStartBot = async () => {
if (actionInFlightRef.current) return; // NEW: block double-clicks / double-fire
actionInFlightRef.current = true;

try {
    setLoading(true);
    const userTickers = await userAPI.getWatchlist();
    if (userTickers.length > 0) {
        try { await hftApiService.bulkUpdateWatchlist(userTickers, 'ADD'); } catch {}
    }
    await hftApiService.startBot();
    setBotRunKey(k => k + 1);
    setBotData(prev => ({ ...prev, isRunning: true }));
    setGlobalBotStatus('INITIALIZING');
    toast.success('Bot started! Wait for analysis to finish before results appear.');

    if (fastPollRef.current) {                 // NEW: clear any stray previous poller
        clearInterval(fastPollRef.current);
        fastPollRef.current = null;
    }

    // Poll every 4s for up to 60s so INITIALIZING doesn't get stuck on a bad tick
    let attempts = 0;
    fastPollRef.current = setInterval(async () => {   // NEW: store in ref, not local var
        attempts++;
        const seq = ++botStatusSeqRef.current;          // NEW: share the staleness guard
        try {
            const res = await hftApiService.getBotStatus();
            if (seq !== botStatusSeqRef.current) return;  // NEW: ignore stale response
            setGlobalBotStatus(res.status);
            
            if (res.status === 'READY' || attempts >= 15) {
                clearInterval(fastPollRef.current!);
                fastPollRef.current = null;
                if (attempts >= 15 && res.status !== 'READY') {
                    setGlobalBotStatus('READY'); // NEW: don't leave button stuck disabled forever
                }
            }
        } catch {
            if (attempts >= 15) {
                clearInterval(fastPollRef.current!);
                fastPollRef.current = null;
                setGlobalBotStatus('READY'); // NEW: fail-safe so button doesn't stay stuck
            }
        }
    }, 4000);

    setTimeout(() => refreshData(), 3000);
} catch (error) {
    console.error('Error starting bot:', error);
    toast.error('Failed to start bot');
} finally {
    setLoading(false);
    actionInFlightRef.current = false; // NEW: release the guard
}
};
    const handleStopBot = async () => {
        try {
            setLoading(true);
            await hftApiService.stopBot();
            setBotData(prev => ({ ...prev, isRunning: false }));
            setGlobalBotStatus('STOPPED');
            toast.success('Bot stopped successfully!');
            await refreshData();
        } catch (error) {
            console.error('Error stopping bot:', error);
            // Always mark as stopped so UI is not stuck when backend is down or request fails
            setBotData(prev => ({ ...prev, isRunning: false }));
            setGlobalBotStatus('STOPPED');
            toast.error('Failed to stop bot (backend may be offline)');
        } finally {
            setLoading(false);
        }
    };

    const handleAddTicker = async (ticker: string) => {
        try {
            // Normalize ticker format
            const normalizedTicker = ticker.toUpperCase().trim();
            const tickerToAdd = normalizedTicker.endsWith('.NS') || normalizedTicker.endsWith('.BO')
                ? normalizedTicker
                : normalizedTicker + '.NS';

            // Call backend API
            const response = await hftApiService.addToWatchlist(tickerToAdd);

            // Update UI immediately with response data
            setBotData(prev => ({
                ...prev,
                config: {
                    ...prev.config,
                    tickers: response.tickers || []
                }
            }));

            toast.success(response.message || `Added ${tickerToAdd} to watchlist`);
        } catch (error) {
            console.error('Error adding ticker:', error);
            toast.error('Failed to add ticker');
            // Refresh to get correct state on error
            await refreshData();
        }
    };

    const handleRemoveTicker = async (ticker: string) => {
        try {
            // Normalize ticker format
            const normalizedTicker = ticker.toUpperCase().trim();
            const tickerToRemove = normalizedTicker.endsWith('.NS') || normalizedTicker.endsWith('.BO')
                ? normalizedTicker
                : normalizedTicker + '.NS';

            // Call backend API
            const response = await hftApiService.removeFromWatchlist(tickerToRemove);

            // Update UI immediately with response data
            setBotData(prev => ({
                ...prev,
                config: {
                    ...prev.config,
                    tickers: response.tickers || []
                }
            }));

            toast.success(response.message || `Removed ${tickerToRemove} from watchlist`);
        } catch (error) {
            console.error('Error removing ticker:', error);
            toast.error('Failed to remove ticker');
            // Refresh to get correct state on error
            await refreshData();
        }
    };

    const handleSaveSettings = async (settings: any) => {
        try {
            setLoading(true);
            const result = await hftApiService.updateSettings(settings);
            if (result.mode === 'paper' || result.mode === 'live') {
                setBotData(prev => ({
                    ...prev,
                    config: {
                        ...prev.config,
                        mode: result.mode as HftTradingMode,
                    },
                }));
            }
            if (result.reverted) {
                toast.error(result.message || 'Live mode unavailable; reverted to paper mode');
            } else {
                toast.success(result.message || 'Settings saved successfully!');
            }
            setShowSettings(false);
            const savedMode: HftTradingMode = result.mode === 'live' ? 'live' : 'paper';
            if (savedMode === 'paper') {
                setLiveStatus(null);
            }
            // Refresh data multiple times to ensure mode is reflected
            await refreshData();
            await new Promise(resolve => setTimeout(resolve, 500)); // Wait 500ms
            await refreshData();
            if (savedMode === 'live') {
                await loadLiveStatus('live'); // Explicitly reload live status
            }
        } catch (error) {
            console.error('Error saving settings:', error);
            toast.error('Failed to save settings');
        } finally {
            setLoading(false);
        }
    };

    const tradingMode: HftTradingMode = botData.config?.mode === 'live' ? 'live' : 'paper';
    const cash = botData.portfolio.cash || 0;

    // Invested value: from Dhan API (cost basis). Fall back to computing if not sent.
    const computedInvested = Object.values(botData.portfolio.holdings || {}).reduce((sum: number, h: any) => {
        const avg: number = parseFloat(h.avgPrice || h.avg_price || 0);
        const qty: number = parseInt(h.quantity || h.qty || 0);
        return sum + (avg * qty);
    }, 0) as number;

    const investedValue: number = computedInvested > 0
        ? computedInvested
        : (botData.portfolio.investedValue != null ? botData.portfolio.investedValue : 0);

    // Today's gain: from Dhan positions unrealizedProfit
    const todayGain = botData.portfolio.todayGain ?? 0;
    const todayGainPct = investedValue > 0 ? (todayGain / investedValue) * 100 : 0;
    const positionsCount = Object.keys(botData.portfolio.holdings).length;

    const cardBg = isLight ? 'bg-white' : isSpace ? 'bg-slate-800/80' : 'bg-slate-800';
    const cardBorder = isLight ? 'border-gray-200' : isSpace ? 'border-purple-900/30' : 'border-slate-700';
    const textPrimary = isLight ? 'text-gray-900' : 'text-white';
    const textMuted = isLight ? 'text-gray-600' : 'text-gray-400';

    return (
        <>
            <Toaster position="top-right" />
            <Layout>
                <div className={`space-y-3 md:space-y-4 w-full ${isLight ? '' : 'animate-fadeIn'}`}>
                    {/* Header: title + status + refresh (same structure as main dashboard) */}
                    <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-2">
                        <div className="flex-1 min-w-0">
                            <div className="flex items-center gap-2 mb-1">
                                <h1 className={`text-xl md:text-2xl font-bold ${textPrimary}`}>Trading</h1>
                                <div className="flex items-center gap-2">
                                    {/* System Connection */}
                                    {connected ? (
                                        <div className="flex items-center gap-1.5 px-2 py-1 bg-green-500/10 border border-green-500/30 rounded-lg flex-shrink-0">
                                            <div className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse"></div>
                                            <span className="text-green-400 text-[10px] font-bold uppercase tracking-wider">System Online</span>
                                        </div>
                                    ) : (
                                        <div className="flex items-center gap-1.5 px-2 py-1 bg-red-500/20 border border-red-500/50 rounded-lg flex-shrink-0">
                                            <AlertCircle className="w-3 h-3 text-red-400" />
                                            <span className="text-red-400 text-[10px] font-bold uppercase tracking-wider">System Offline</span>
                                        </div>
                                    )}

                                    {/* Trading Mode */}
                                    {connected && (
                                        <div
                                            className={`flex items-center gap-1.5 px-2 py-1 border rounded-lg flex-shrink-0 ${tradingMode === 'paper'
                                                ? 'bg-blue-500/10 border-blue-500/30'
                                                : 'bg-red-500/10 border-red-500/30'
                                                }`}
                                            title={tradingMode === 'paper' ? 'Paper mode: simulated trades only' : 'Live mode: broker-backed trading'}
                                        >
                                            <span className={`text-[10px] font-bold uppercase tracking-wider ${tradingMode === 'paper' ? 'text-blue-400' : 'text-red-400'
                                                }`}>
                                                {tradingMode === 'paper' ? 'Paper Mode' : 'Live Mode'}
                                            </span>
                                        </div>
                                    )}

                                    {/* Broker Connection */}
                                    {connected && tradingMode === 'live' && (
                                        liveStatus?.connected ? (
                                            <div className="flex items-center gap-1.5 px-2 py-1 bg-blue-500/10 border border-blue-500/30 rounded-lg flex-shrink-0" title="Broker: Dhan connection validated">
                                                <CheckCircle2 className="w-3 h-3 text-blue-400" />
                                                <span className="text-blue-400 text-[10px] font-bold uppercase tracking-wider">Broker Connected</span>
                                            </div>
                                        ) : (
                                            <div
                                                className="flex items-center gap-1.5 px-2 py-1 bg-amber-500/10 border border-amber-500/30 rounded-lg flex-shrink-0 cursor-help"
                                                title={liveStatus?.dhan_error || "Broker authentication required"}
                                            >
                                                <AlertCircle className="w-3 h-3 text-amber-500" />
                                                <span className="text-amber-500 text-[10px] font-bold uppercase tracking-wider">Broker: Action Required</span>
                                            </div>
                                        )
                                    )}
                                </div>
                            </div>
                            <p className={`text-xs md:text-sm ${textMuted}`}>
                                Updated {new Date().toLocaleTimeString()}
                            </p>
                            {connected && liveStatus?.dhan_error && (
                                <p className="text-xs mt-1 text-amber-500 dark:text-amber-400 flex items-center gap-1 animate-pulse">
                                    <AlertCircle className="w-3 h-3" />
                                    Broker Status: {liveStatus.dhan_error}
                                </p>
                            )}
                        </div>
                        <button
                            onClick={refreshData}
                            disabled={loading}
                            className="flex items-center justify-center gap-1.5 px-4 py-2.5 bg-blue-500 hover:bg-blue-600 text-white rounded-lg text-sm font-semibold transition-all disabled:opacity-50 w-full md:w-auto min-h-[44px] md:min-h-0"
                        >
                            <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
                            Refresh
                        </button>
                    </div>

                    {/* Portfolio metrics row */}
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                        <div className={`${cardBg} border ${cardBorder} rounded-xl p-4`}>
                            <p className={`text-xs font-medium uppercase tracking-wide ${textMuted}`}>Invested Value</p>
                            <p className={`text-lg font-bold ${textPrimary}`}>{formatCurrency(investedValue)}</p>
                        </div>
                        <div className={`${cardBg} border ${cardBorder} rounded-xl p-4`}>
                            <p className={`text-xs font-medium uppercase tracking-wide ${textMuted}`}>Cash</p>
                            <p className={`text-lg font-bold ${textPrimary}`}>{formatCurrency(cash)}</p>
                        </div>
                        <div className={`${cardBg} border ${cardBorder} rounded-xl p-4`}>
                            <p className={`text-xs font-medium uppercase tracking-wide ${textMuted}`}>Today's Gains</p>
                            <p className={`text-lg font-bold ${textPrimary}`}>{formatCurrency(todayGain)}</p>
                            <p className={`text-sm font-semibold ${todayGainPct >= 0 ? 'text-green-500' : 'text-red-500'}`}>
                                {formatPercentage(todayGainPct)}
                            </p>
                        </div>
                        <div className={`${cardBg} border ${cardBorder} rounded-xl p-4`}>
                            <p className={`text-xs font-medium uppercase tracking-wide ${textMuted}`}>Positions</p>
                            <p className={`text-lg font-bold ${textPrimary}`}>{positionsCount}</p>
                        </div>
                    </div>

                    {/* Quick actions */}
                    <div className="flex flex-wrap gap-2">
                        <button
                            onClick={handleStartBot}
                            disabled={botData.isRunning || globalBotStatus === 'INITIALIZING'}
                            className="flex items-center gap-2 px-4 py-2.5 bg-green-600 hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed text-white rounded-lg text-sm font-semibold transition-all"
                        >
                            {globalBotStatus === 'INITIALIZING' ? (
                                <><Loader2 className="w-4 h-4 animate-spin" /> Initializing...</>
                            ) : (
                                <><Play className="w-4 h-4" /> {tradingMode === 'paper' ? 'Start Paper Trading' : 'Start Trading'}</>
                            )}
                        </button>
                        <button
                            onClick={handleStopBot}
                            disabled={!botData.isRunning}
                            className="flex items-center gap-2 px-4 py-2.5 bg-red-600 hover:bg-red-700 disabled:opacity-50 disabled:cursor-not-allowed text-white rounded-lg text-sm font-semibold transition-all"
                        >
                            <><Square className="w-4 h-4" /> Stop Trading</>
                        </button>
                        <button
                            onClick={() => setShowSettings(true)}
                            disabled={botData.isRunning}
                            className="flex items-center gap-2 px-4 py-2.5 bg-slate-600 hover:bg-slate-700 disabled:opacity-50 text-white rounded-lg text-sm font-semibold transition-all"
                        >
                            Settings
                        </button>
                    </div>

                    {/* Tabs (Dashboard / Portfolio / Chat) */}
                    <div className={`${cardBg} border ${cardBorder} rounded-xl overflow-hidden`}>
                        <div className={`flex border-b ${cardBorder} p-1 gap-1`}>
                            {[
                                { id: 'dashboard' as const, label: 'Dashboard', icon: LayoutDashboard },
                                { id: 'portfolio' as const, label: 'Portfolio', icon: Briefcase },
                                { id: 'activity' as const, label: 'Recent Trading Activity', icon: MessageCircle },
                                { id: 'watchlist' as const, label: 'Watchlist', icon: CheckCircle2 },
                            ].map(({ id, label, icon: Icon }) => (
                                <button
                                    key={id}
                                    onClick={() => setActiveTab(id)}
                                    className={`flex items-center gap-2 px-4 py-3 rounded-lg text-sm font-medium transition-all ${activeTab === id
                                        ? isLight ? 'bg-blue-500 text-white' : 'bg-blue-600 text-white'
                                        : isLight ? 'text-gray-600 hover:bg-gray-100' : 'text-gray-400 hover:bg-slate-700'
                                        }`}
                                >
                                    <Icon className="w-4 h-4" /> {label}
                                </button>
                            ))}
                        </div>
                        <div className="p-4 md:p-6 min-h-[400px]">
                            {/* Always show components regardless of trading mode or connection status */}
                            {activeTab === 'dashboard' && <HftDashboard botData={botData} botRunKey={botRunKey} onRefresh={refreshData} />}
                            {(activeTab === 'portfolio' || activeTab === 'activity' || activeTab === 'watchlist') && (
                                <HftPortfolio
                                    activeSection={activeTab}
                                    botData={botData}
                                    botRunKey={botRunKey}
                                    onAddTicker={handleAddTicker}
                                    onRemoveTicker={handleRemoveTicker}
                                    onRefresh={refreshData}
                                />
                            )}
                        </div>
                    </div>
                </div>

                {loading && <HftLoadingOverlay />}
                {showSettings && (
                    <HftSettingsModal
                        settings={botData.config}
                        onSave={handleSaveSettings}
                        onRefresh={refreshData}
                        onClose={() => setShowSettings(false)}
                    />
                )}
            </Layout>
        </>
    );
}
