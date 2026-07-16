import sys
sys.stdout.reconfigure(encoding='utf-8')

# Verify testindia.py
with open(r'backend\hft2\backend\testindia.py', 'r', encoding='utf-8') as f:
    t = f.read()

checks = [
    ('buy() paper mode check', 'if self.mode == "paper":\n                # Paper trading: simulate locally, no broker needed\n                logger.info(f"[PAPER] SIMULATED BUY'),
    ('sell() paper mode check', 'if self.mode == "paper":\n                # Paper trading: simulate locally, no broker needed\n                logger.info(f"[PAPER] SIMULATED SELL'),
    ('buy() live mode guard', 'if not self.api:\n                    logger.error("Broker API not initialized - cannot execute live trade")\n                    return False\n                order_result = self.api.place_order(\n                    security_id=self.get_security_id(asset),\n                    exchange_segment="NSE_EQ",\n                    transaction_type="BUY"'),
    ('sell() live mode guard', 'if not self.api:\n                    logger.error("Broker API not initialized - cannot execute live trade")\n                    return False\n                order_result = self.api.place_order(\n                    security_id=self.get_security_id(asset),\n                    exchange_segment="NSE_EQ",\n                    transaction_type="SELL"'),
    ('old broker-only buy gone', '# Place actual order via Dhan API (live trading only)\n            if self.api:\n                order_result'),
]

print("=== testindia.py ===")
for name, snippet in checks:
    found = snippet in t
    if name.startswith('old') and not found:
        print(f"[OK] {name} (correctly removed)")
    elif not name.startswith('old') and found:
        print(f"[OK] {name}")
    else:
        print(f"[FAIL] {name}")

# Verify web_backend.py
with open(r'backend\hft2\backend\web_backend.py', 'r', encoding='utf-8') as f:
    w = f.read()

web_checks = [
    ('paper mode disabled gone', 'Paper mode is disabled. Manual orders only supported in live mode.'),
    ('paper order execution present', 'Paper mode: simulate trade via VirtualPortfolio'),
    ('paper portfolio.buy call', 'ok = portfolio.buy(request.symbol, request.quantity, price)'),
    ('paper portfolio.sell call', 'ok = portfolio.sell(request.symbol, request.quantity, price)'),
    ('loop paper trade path', 'elif current_bot_mode == "paper":'),
    ('loop paper buy', 'ok = await loop.run_in_executor(None, lambda: portfolio.buy(sym, qty, price))'),
]

print("\n=== web_backend.py ===")
for name, snippet in web_checks:
    found = snippet in w
    if name.startswith('paper mode disabled') and not found:
        print(f"[OK] {name} (correctly removed)")
    elif not name.startswith('paper mode disabled') and found:
        print(f"[OK] {name}")
    else:
        print(f"[FAIL] {name}")
