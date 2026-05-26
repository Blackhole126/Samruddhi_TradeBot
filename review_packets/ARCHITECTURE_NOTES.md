# ARCHITECTURE_NOTES

# CORE ARCHITECTURE

Observed architecture:

Client
→ FastAPI Layer
→ MCP Adapter
→ Prediction Engine
→ Feature Engineering
→ Signal Layer
→ Execution Layer
→ Portfolio Layer
→ Observability Layer

---

# MAJOR COMPONENTS

| Component | Role |
|---|---|
| api_server.py | API gateway |
| MCPAdapter | orchestration layer |
| stock_analysis_complete.py | prediction engine |
| live_executor.py | broker execution |
| dhan_client.py | broker communication |
| monitoring.py | observability |
| performance_monitor.py | runtime metrics |
| production_monitor.py | production monitoring |

---

# EXECUTION GOVERNANCE

Observed governance improvements:
- structured logging
- request lineage continuity
- replay-aware execution tracking
- broker acknowledgement visibility
- deterministic failure propagation

---

# STATE GOVERNANCE

Observed state regions:
- runtime caches
- async execution loops
- websocket managers
- replay lineage structures
- portfolio persistence layers

---

# DEPLOYMENT FOUNDATIONS

Observed deployment readiness:
- Dockerfiles present
- requirements files pinned
- startup scripts present
- Linux deployment readiness partially prepared

---

# ARCHITECTURE STATUS

System architecture demonstrates:
- modular execution layering
- observable runtime flow
- replay-capable foundations
- broker alignment preparation