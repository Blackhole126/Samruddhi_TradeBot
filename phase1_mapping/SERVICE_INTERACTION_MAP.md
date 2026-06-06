# SERVICE_INTERACTION_MAP.md

# Service Interaction Map

Frontend Dashboard
    ↓
api_server.py
    ↓
web_backend.py
    ↓
Authentication Layer
    ↓
Execution Validation
    ↓
execution_tool.py
    ↓
live_executor.py
    ↓
broker_adapter.py
    ↓
dhan_client.py
    ↓
Dhan Broker API

---

# Persistence Interaction

live_executor.py
    ↓
portfolio_manager.py
    ↓
SQLite Database

---

# Runtime State Interaction

web_backend.py
    ↔ user_state

execution_tool.py
    ↔ active_orders

live_executor.py
    ↔ pending_orders

dhan_client.py
    ↔ portfolio cache

---

# Observability Interaction

Execution Layer
    ↓
.runlogs/

Execution Layer
    ↓
karma_logs/

Execution Layer
    ↓
server_crash_log.txt

---

# Simulation / Mock Interaction

execution_router.py
    ↓
shadow_execution/simulator.py

paper trading stubs
    ↓
local simulation state

---

# Identified Architectural Risks

1. Legacy execution bypass exists
2. Multiple runtime truth regions exist
3. Multiple cache authorities exist
4. Replay-sensitive transient state exists
5. Full deterministic replay convergence not yet complete