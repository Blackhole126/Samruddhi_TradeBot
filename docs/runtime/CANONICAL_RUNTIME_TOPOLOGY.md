# Canonical Runtime Topology

## Intended Canonical Execution Spine

Client/API
→ api_server.py
→ mcp_adapter.py
→ prediction/signal pipeline
→ ExecutionTool
→ LiveTradingExecutor
→ dhan_client.py
→ persistence layer
→ observability layer
→ replay/audit persistence

---

## Positive Convergence Signals

- Execution authority is increasingly centralized.
- LiveTradingExecutor behaves as canonical execution authority.
- Replay awareness has significantly improved.
- Audit persistence infrastructure exists.
- Deployment/runtime maturity has improved.

---

## Remaining Fragmentation Regions

| Region | Risk |
|---|---|
| Multiple API runtimes | Distributed runtime authority |
| Async runtime layers | Detached lineage |
| WebSocket/SSE state | Replay discontinuity |
| Shadow execution systems | Mock/live ambiguity |
| Distributed persistence | Non-canonical replay behavior |

---

## Final Phase 1 Findings

- System convergence maturity has significantly improved.
- Runtime execution ordering is increasingly deterministic.
- Replay continuity remains partially incomplete.
- Observability continuity remains partially fragmented.
- Canonical trace lineage is not yet fully unified.
- Broker truth anchoring remains partially incomplete.
- Hidden runtime state still exists across async regions.



## Execution Topology Diagram

```text
Client/API
    ↓
api_server.py
    ↓
mcp_adapter.py
    ↓
Prediction / Signal Pipeline
    ↓
ExecutionTool
    ↓
LiveTradingExecutor
    ↓
broker_adapter.py
    ↓
dhan_client.py
    ↓
Persistence Layer
    ├── samruddhi_memory.py
    ├── decision_audit_trail.py
    └── portfolio persistence
    ↓
Observability Layer
    ├── monitoring.py
    ├── audit trail
    └── runtime logging
    ↓
Replay / Reconstruction Layer
```