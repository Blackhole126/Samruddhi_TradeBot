# DEPENDENCY_GRAPH.md

# High-Level Dependency Graph

Frontend Dashboard
    ↓
api_server.py
    ↓
web_backend.py
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

# Persistence Layer

live_executor.py
    ↓
portfolio_manager.py
    ↓
SQLite Database

---

# Runtime State Dependencies

web_backend.py
    ↓
user_state

execution_tool.py
    ↓
active_orders

live_executor.py
    ↓
pending_orders

---

# Cache Dependencies

request_cache.py
data_service_client.py
multi_source_data_provider.py
dhan_client.py
stock_analysis_complete.py

---

# Observability Dependencies

.runlogs/
karma_logs/
server_crash_log.txt

---

# Simulation Dependencies

execution_router.py
shadow_execution/simulator.py
paper trading stubs