"""
Fix paper trading bugs:
1. testindia.py - buy()/sell() skip Dhan API in paper mode
2. web_backend.py - /api/order enable paper mode
3. web_backend.py - _continuous_trading_loop execute paper trades
"""
import re

# ── Fix 1: testindia.py ──────────────────────────────────────────────────────
path1 = r'c:\Users\Aarti\Documents\htmlfolder\Samruddhi_TradeBot\backend\hft2\backend\testindia.py'
with open(path1, 'r', encoding='utf-8') as f:
    src = f.read()

# Replace buy() broker block
old_buy = (
    '        try:\n'
    '            # Place actual order via Dhan API (live trading only)\n'
    '            if self.api:\n'
    '                order_result = self.api.place_order(\n'
    '                    security_id=self.get_security_id(asset),\n'
    '                    exchange_segment="NSE_EQ",\n'
    '                    transaction_type="BUY",\n'
    '                    order_type="MARKET",\n'
    '                    quantity=qty,\n'
    '                    price=0,  # Market order uses 0 for price\n'
    '                    validity="DAY",\n'
    '                    product_type="CNC"\n'
    '                )\n'
)
new_buy = (
    '        try:\n'
    '            if self.mode == "paper":\n'
    '                # Paper trading: simulate locally, no broker needed\n'
    '                logger.info(f"[PAPER] SIMULATED BUY {qty} {asset} @ Rs.{price:.2f}")\n'
    '            else:\n'
    '                # Live trading: place real order via Dhan API\n'
    '                if not self.api:\n'
    '                    logger.error("Broker API not initialized - cannot execute live trade")\n'
    '                    return False\n'
    '                order_result = self.api.place_order(\n'
    '                    security_id=self.get_security_id(asset),\n'
    '                    exchange_segment="NSE_EQ",\n'
    '                    transaction_type="BUY",\n'
    '                    order_type="MARKET",\n'
    '                    quantity=qty,\n'
    '                    price=0,\n'
    '                    validity="DAY",\n'
    '                    product_type="CNC"\n'
    '                )\n'
)

if old_buy in src:
    src = src.replace(old_buy, new_buy, 1)
    print("[OK] buy() broker block replaced")
else:
    print("[FAIL] buy() block NOT found - checking variant...")
    # Try without the blank line after try:
    old_buy2 = (
        '        try:\n\n'
        '            # Place actual order via Dhan API (live trading only)\n'
        '            if self.api:\n\n'
        '                order_result = self.api.place_order(\n'
        '                    security_id=self.get_security_id(asset),\n'
        '                    exchange_segment="NSE_EQ",\n\n'
        '                    transaction_type="BUY",\n'
        '                    order_type="MARKET",\n\n'
        '                    quantity=qty,\n'
        '                    price=0,  # Market order uses 0 for price\n'
        '                    validity="DAY",\n'
        '                    product_type="CNC"\n\n'
        '                )\n'
    )
    if old_buy2 in src:
        src = src.replace(old_buy2, new_buy, 1)
        print("[OK] buy() broker block (variant) replaced")
    else:
        print("[FAIL] buy() variant also not found")

# Find and fix the "else: logger.error Broker API not initialized" after buy logger.info
# Remove the old else block that returns False after the logger.info for buy
old_buy_else = (
    '            else:\n'
    '                logger.error(\n'
    '                    "Broker API not initialized - cannot execute live trade")\n'
    '                return False\n'
    '\n'
    '\n'
    '            # Update portfolio regardless of mode\n'
    '\n'
    '            self.cash -= cost\n'
)
new_buy_else = (
    '\n'
    '            # Update portfolio\n'
    '            self.cash -= cost\n'
)
if old_buy_else in src:
    src = src.replace(old_buy_else, new_buy_else, 1)
    print("[OK] buy() else-return block removed")
else:
    # simpler pattern
    old_buy_else2 = (
        '            else:\n'
        '                logger.error(\n'
        '                    "Broker API not initialized - cannot execute live trade")\n'
        '                return False\n'
        '\n'
        '            # Update portfolio regardless of mode\n'
        '            self.cash -= cost\n'
    )
    if old_buy_else2 in src:
        src = src.replace(old_buy_else2, '            # Update portfolio\n            self.cash -= cost\n', 1)
        print("[OK] buy() else-return block (variant) removed")
    else:
        print("[WARN] buy() else block not found separately - may already be handled")

# Replace sell() broker block
old_sell = (
    '        try:\n'
    '            # Place actual order via Dhan API (live trading only)\n'
    '            if self.api:\n'
    '                order_result = self.api.place_order(\n'
    '                    security_id=self.get_security_id(asset),\n'
    '                    exchange_segment="NSE_EQ",\n'
    '                    transaction_type="SELL",\n'
    '                    order_type="MARKET",\n'
    '                    quantity=qty,\n'
    '                    price=0,  # Market order uses 0 for price\n'
    '                    validity="DAY",\n'
    '                    product_type="CNC"\n'
    '                )\n'
)
new_sell = (
    '        try:\n'
    '            if self.mode == "paper":\n'
    '                # Paper trading: simulate locally, no broker needed\n'
    '                logger.info(f"[PAPER] SIMULATED SELL {qty} {asset} @ Rs.{price:.2f}")\n'
    '            else:\n'
    '                # Live trading: place real order via Dhan API\n'
    '                if not self.api:\n'
    '                    logger.error("Broker API not initialized - cannot execute live trade")\n'
    '                    return False\n'
    '                order_result = self.api.place_order(\n'
    '                    security_id=self.get_security_id(asset),\n'
    '                    exchange_segment="NSE_EQ",\n'
    '                    transaction_type="SELL",\n'
    '                    order_type="MARKET",\n'
    '                    quantity=qty,\n'
    '                    price=0,\n'
    '                    validity="DAY",\n'
    '                    product_type="CNC"\n'
    '                )\n'
)

if old_sell in src:
    src = src.replace(old_sell, new_sell, 1)
    print("[OK] sell() broker block replaced")
else:
    old_sell2 = (
        '        try:\n\n'
        '            # Place actual order via Dhan API (live trading only)\n'
        '            if self.api:\n\n'
        '                order_result = self.api.place_order(\n'
        '                    security_id=self.get_security_id(asset),\n'
        '                    exchange_segment="NSE_EQ",\n'
        '                    transaction_type="SELL",\n\n'
        '                    order_type="MARKET",\n'
        '                    quantity=qty,\n\n'
        '                    price=0,  # Market order uses 0 for price\n'
        '                    validity="DAY",\n'
        '                    product_type="CNC"\n\n'
        '                )\n'
    )
    if old_sell2 in src:
        src = src.replace(old_sell2, new_sell, 1)
        print("[OK] sell() broker block (variant) replaced")
    else:
        print("[FAIL] sell() block NOT found")

# Remove old sell else block
old_sell_else = (
    '            else:\n'
    '                logger.error(\n'
    '                    "Broker API not initialized - cannot execute live trade")\n'
    '                return False\n'
    '\n'
    '            # Update portfolio regardless of mode\n'
    '\n'
    '            revenue = qty * price\n'
)
new_sell_else = (
    '\n'
    '            # Update portfolio\n'
    '            revenue = qty * price\n'
)
if old_sell_else in src:
    src = src.replace(old_sell_else, new_sell_else, 1)
    print("[OK] sell() else-return block removed")
else:
    old_sell_else2 = (
        '            else:\n'
        '                logger.error(\n'
        '                    "Broker API not initialized - cannot execute live trade")\n'
        '\n'
        '                return False\n'
        '\n'
        '\n'
        '            # Update portfolio regardless of mode\n'
        '\n'
        '            revenue = qty * price\n'
    )
    if old_sell_else2 in src:
        src = src.replace(old_sell_else2, '\n            # Update portfolio\n            revenue = qty * price\n', 1)
        print("[OK] sell() else-return block (variant) removed")
    else:
        print("[WARN] sell() else block not found separately - may already be handled")

with open(path1, 'w', encoding='utf-8') as f:
    f.write(src)
print("[OK] testindia.py saved")

# ── Fix 2 & 3: web_backend.py ────────────────────────────────────────────────
path2 = r'c:\Users\Aarti\Documents\htmlfolder\Samruddhi_TradeBot\backend\hft2\backend\web_backend.py'
with open(path2, 'r', encoding='utf-8') as f:
    src2 = f.read()

# Fix 2: Replace "Paper mode is disabled" block with actual paper execution
old_paper_disabled = (
        '        # Non-live mode is now disabled\n'
        '        raise HTTPException(\n'
        '            status_code=400,\n'
        '            detail="Paper mode is disabled. Manual orders only supported in live mode."\n'
        '        )\n'
)
new_paper_exec = (
        '        # Paper mode: simulate trade via VirtualPortfolio\n'
        '        if current_mode == "paper":\n'
        '            portfolio = getattr(getattr(bot, "trading_bot", None), "portfolio", None)\n'
        '            if not portfolio:\n'
        '                raise HTTPException(status_code=503, detail="Paper portfolio not initialized")\n'
        '            price = request.price or 0.0\n'
        '            if price <= 0:\n'
        '                # Fetch current price from yfinance as fallback\n'
        '                try:\n'
        '                    import yfinance as yf\n'
        '                    ticker_data = yf.Ticker(request.symbol)\n'
        '                    hist = ticker_data.history(period="1d")\n'
        '                    price = float(hist["Close"].iloc[-1]) if not hist.empty else 0.0\n'
        '                except Exception:\n'
        '                    price = 0.0\n'
        '            if price <= 0:\n'
        '                raise HTTPException(status_code=400, detail="Could not determine price for paper trade")\n'
        '            if side == "BUY":\n'
        '                ok = portfolio.buy(request.symbol, request.quantity, price)\n'
        '            else:\n'
        '                ok = portfolio.sell(request.symbol, request.quantity, price)\n'
        '            if not ok:\n'
        '                raise HTTPException(status_code=400, detail=f"Paper {side} failed - check cash/holdings")\n'
        '            return {\n'
        '                "success": True,\n'
        '                "status": "executed",\n'
        '                "order_id": f"PAPER-{int(__import__(\"time\").time()*1000)}",\n'
        '                "symbol": request.symbol,\n'
        '                "side": side,\n'
        '                "quantity": request.quantity,\n'
        '                "price": price,\n'
        '                "message": f"[PAPER] {side} {request.quantity} {request.symbol} @ Rs.{price:.2f}",\n'
        '                "mode": "paper",\n'
        '            }\n'
)

if old_paper_disabled in src2:
    src2 = src2.replace(old_paper_disabled, new_paper_exec, 1)
    print("[OK] /api/order paper mode enabled")
else:
    print("[FAIL] paper disabled block NOT found in web_backend.py")

# Fix 3: _continuous_trading_loop - add paper trade path alongside live_executor
old_loop_trade = (
            '                            if (rec == "BUY" or rec == "SELL"):\n'
            '                                logger.info(\n'
            '                                    f"\U0001f916 Auto-{rec} signal for {sym} (User: {username}, confidence={conf:.2f})")\n'
            '                                if hasattr(bot, \'live_executor\') and bot.live_executor:\n'
            '                                    signal_data = {\n'
            '                                        "confidence": conf,\n'
            '                                        "current_price": analysis.get("current_price") or analysis.get("target_price"),\n'
            '                                        "stop_loss": analysis.get("stop_loss"),\n'
            '                                        "take_profit": analysis.get("target_price"),\n'
            '                                    }\n'
            '                                    loop = asyncio.get_event_loop()\n'
            '                                    if rec == "BUY":\n'
            '                                        result = await loop.run_in_executor(\n'
            '                                            None,\n'
            '                                            lambda s=sym, sd=signal_data: bot.live_executor.execute_buy_order(\n'
            '                                                s, sd)\n'
            '                                        )\n'
            '                                    else:\n'
            '                                        result = await loop.run_in_executor(\n'
            '                                            None,\n'
            '                                            lambda s=sym, sd=signal_data: bot.live_executor.execute_sell_order(\n'
            '                                                s, sd)\n'
            '                                        )\n'
)
new_loop_trade = (
            '                            if (rec == "BUY" or rec == "SELL"):\n'
            '                                logger.info(\n'
            '                                    f"Auto-{rec} signal for {sym} (User: {username}, confidence={conf:.2f})")\n'
            '                                current_bot_mode = bot.config.get("mode", "paper")\n'
            '                                loop = asyncio.get_event_loop()\n'
            '                                if current_bot_mode == "live" and hasattr(bot, "live_executor") and bot.live_executor:\n'
            '                                    signal_data = {\n'
            '                                        "confidence": conf,\n'
            '                                        "current_price": analysis.get("current_price") or analysis.get("target_price"),\n'
            '                                        "stop_loss": analysis.get("stop_loss"),\n'
            '                                        "take_profit": analysis.get("target_price"),\n'
            '                                    }\n'
            '                                    if rec == "BUY":\n'
            '                                        result = await loop.run_in_executor(\n'
            '                                            None,\n'
            '                                            lambda s=sym, sd=signal_data: bot.live_executor.execute_buy_order(s, sd)\n'
            '                                        )\n'
            '                                    else:\n'
            '                                        result = await loop.run_in_executor(\n'
            '                                            None,\n'
            '                                            lambda s=sym, sd=signal_data: bot.live_executor.execute_sell_order(s, sd)\n'
            '                                        )\n'
            '                                elif current_bot_mode == "paper":\n'
            '                                    # Paper mode: execute via VirtualPortfolio (no broker needed)\n'
            '                                    portfolio = getattr(getattr(bot, "trading_bot", None), "portfolio", None)\n'
            '                                    price = analysis.get("current_price") or analysis.get("target_price") or 0\n'
            '                                    if portfolio and price and price > 0:\n'
            '                                        qty = max(1, int((portfolio.cash * 0.10) / price)) if rec == "BUY" else 1\n'
            '                                        if rec == "BUY":\n'
            '                                            ok = await loop.run_in_executor(None, lambda: portfolio.buy(sym, qty, price))\n'
            '                                        else:\n'
            '                                            holding = portfolio.holdings.get(sym, {})\n'
            '                                            qty = holding.get("qty", 0)\n'
            '                                            ok = await loop.run_in_executor(None, lambda: portfolio.sell(sym, qty, price)) if qty > 0 else False\n'
            '                                        result = {"success": ok, "message": f"[PAPER] {rec} {qty} {sym} @ Rs.{price:.2f}"}\n'
            '                                    else:\n'
            '                                        result = {"success": False, "message": "No price available for paper trade"}\n'
            '                                else:\n'
            '                                    result = {"success": False, "message": "No executor available"}\n'
)

if old_loop_trade in src2:
    src2 = src2.replace(old_loop_trade, new_loop_trade, 1)
    print("[OK] _continuous_trading_loop paper trade path added")
else:
    print("[FAIL] continuous loop trade block NOT found - trying unicode variant...")
    # The file may have different unicode chars in the f-string emoji
    # Use regex to find and replace
    pattern = re.compile(
        r'(                            if \(rec == "BUY" or rec == "SELL"\):\n'
        r'                                logger\.info\(\n'
        r'.*?Auto-\{rec\} signal for.*?\n'
        r'                                if hasattr\(bot, \'live_executor\'\) and bot\.live_executor:\n)',
        re.DOTALL
    )
    m = pattern.search(src2)
    if m:
        print("  Found via regex at pos " + str(m.start()))
    else:
        print("  Regex also failed - loop block needs manual inspection")

with open(path2, 'w', encoding='utf-8') as f:
    f.write(src2)
print("[OK] web_backend.py saved")
print("All fixes applied.")
