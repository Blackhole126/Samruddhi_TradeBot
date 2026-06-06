# Canonical Execution Flow Map

## Primary Canonical Flow

Client/API
→ backend/api_server.py
→ core/mcp_adapter.py
→ ExecutionTool.execute_trade()
→ LiveTradingExecutor.place_order()
→ dhan_client.place_order()
→ portfolio persistence
→ observability logging
→ replay/audit persistence

---

## Runtime Components

| Stage | Component | File |
|---|---|---|
| API Gateway | FastAPI Runtime | backend/api_server.py |
| Orchestration | MCP Adapter | backend/core/mcp_adapter.py |
| Signal Intelligence | Prediction Engine | backend/stock_analysis_complete.py |
| Trade Execution | ExecutionTool | backend/hft2/backend/mcp_server/tools/execution_tool.py |
| Canonical Execution | LiveTradingExecutor | backend/hft2/backend/live_executor.py |
| Broker Integration | Dhan Client | backend/hft2/backend/dhan_client.py |
| Persistence | Portfolio + Audit | backend/hft2/backend/db/ |
| Observability | Logging + Monitoring | backend/hft2/backend/utils/ |

---

## Async Runtime Regions

| Region | Risk |
|---|---|
| WebSocket broadcasting | Trace fragmentation |
| SSE snapshots | Replay discontinuity |
| Background monitoring threads | Non-deterministic ordering |
| Async signal collectors | Detached lineage |
| Async MCP tools | Distributed observability |

---

## Fragmentation Findings

- Multiple runtime entry points still exist.
- Replay persistence is distributed across subsystems.
- Async execution continuity is partially detached.
- Observability remains partially fragmented.
- Shadow execution systems still coexist with live execution systems.