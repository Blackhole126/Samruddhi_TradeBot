# RUNTIME_EXECUTION_GRAPH.md

# Runtime Execution Flow

User Request
    ↓
Frontend Dashboard
    ↓
API Route
    ↓
web_backend.py
    ↓
Authentication Layer
    ↓
Signal / Execution Validation
    ↓
execution_tool.py
    ↓
live_executor.place_order()
    ↓
Broker Adapter
    ↓
dhan_client.place_order()
    ↓
Broker API
    ↓
Execution Response
    ↓
portfolio_manager.record_trade()
    ↓
SQLite Persistence
    ↓
Observability / Logs
    ↓
Frontend Update

---

# Runtime Replay-Sensitive Regions

| Runtime State | Risk |
|---|---|
| pending_orders | transient execution state |
| active_orders | transient order tracking |
| user_state | runtime orchestration state |
| portfolio cache | stale state risk |
| async execution | detached execution risk |

---

# Async Execution Boundaries

run_in_executor() identified in:
- web_backend.py
- routes.py

Most usages validated as:
- infrastructure tasks
- async wrappers
- portfolio sync

No major hidden broker execution discovered besides legacy bypass path.

---

# Confirmed Replay Concern

Legacy execution path bypasses centralized executor:

simple_app.py
→ place_order_market()
→ dhan_client.py

This introduces:
- replay inconsistency
- fragmented observability
- duplicate execution authority