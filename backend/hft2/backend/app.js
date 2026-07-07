(function () {
  function ensureTradingModeUI() {
    if (document.getElementById('settings-mode-row')) return;

    const target =
      document.getElementById('riskLevel')?.closest('.form-group') ||
      document.querySelector('[name="riskLevel"]')?.closest('.form-group') ||
      document.querySelector('.settings-form') ||
      document.body;

    const row = document.createElement('div');
    row.id = 'settings-mode-row';
    row.className = 'form-group';
    row.style.marginBottom = '12px';

    row.innerHTML = `
      <label style="display:block; margin-bottom:6px; font-weight:600;">Trading Mode</label>
      <div style="display:flex; flex-wrap:wrap; gap:16px; align-items:center; padding:8px 10px; border:1px solid #ccc; border-radius:6px; background:#fff; max-width:260px;">
        <label style="display:flex; align-items:center; gap:6px;">
          <input type="radio" name="tradingMode" value="paper" checked>
          Paper
        </label>
        <label style="display:flex; align-items:center; gap:6px;">
          <input type="radio" name="tradingMode" value="live">
          Live
        </label>
      </div>
    `;

    if (target && target.nodeName === 'BODY') {
      target.appendChild(row);
    } else if (target && target.parentNode) {
      target.parentNode.insertBefore(row, target);
    } else if (document.body) {
      document.body.appendChild(row);
    }
  }

  function getSelectedMode() {
    const selected = document.querySelector('input[name="tradingMode"]:checked');
    return selected ? selected.value : 'paper';
  }

  async function loadSettings() {
    ensureTradingModeUI();

    try {
      const res = await fetch('/api/settings');
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const settings = await res.json();
      const mode = (settings.mode || 'paper').toLowerCase();

      document.querySelectorAll('input[name="tradingMode"]').forEach((radio) => {
        radio.checked = radio.value === mode;
      });
    } catch (err) {
      console.error(err);
    }
  }

  async function saveSettings() {
    ensureTradingModeUI();

    const payload = {
      mode: getSelectedMode(),
      riskLevel: document.getElementById('riskLevel')?.value || 'MEDIUM',
      stop_loss_pct: Number(document.getElementById('stopLossPct')?.value || 0.05),
      target_profit_pct: Number(document.getElementById('targetProfitPct')?.value || 0.1),
      max_capital_per_trade: Number(document.getElementById('maxCapitalPerTrade')?.value || 0.25),
      max_trade_limit: Number(document.getElementById('maxTradeLimit')?.value || 10)
    };

    await fetch('/api/settings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
  }

  function init() {
    ensureTradingModeUI();
    loadSettings().catch(console.error);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.ensureTradingModeUI = ensureTradingModeUI;
  window.getSelectedMode = getSelectedMode;
  window.loadSettings = loadSettings;
  window.saveSettings = saveSettings;
})();