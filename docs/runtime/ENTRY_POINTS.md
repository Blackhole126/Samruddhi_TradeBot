# Runtime Entry Points

## API Runtime Entry Points

| Component | File | Purpose | Runtime Role |
|---|---|---|---|
| FastAPI Main Runtime | backend/api_server.py | Canonical API gateway | Primary backend runtime |
| HFT Runtime | backend/hft2/backend/web_backend.py | Trading runtime + SSE + orchestration | High-frequency execution layer |
| MCP Trading Runtime | backend/hft2/backend/mcp_server/mcp_trading_server.py | MCP orchestration | AI trading coordination |
| HFT App Runtime | backend/hft2/backend/app.py | WebSocket + runtime API | Async execution exposure |
| Simple App Runtime | backend/hft2/backend/simple_app.py | Lightweight execution runtime | Secondary runtime surface |
| HFT Routes | backend/hft/routes.py | Runtime orchestration | Trading route coordination |

---

## Runtime Startup Regions

| Component | Startup Behavior | Runtime Risk |
|---|---|---|
| api_server.py | Starts FastAPI backend | Partial request lineage |
| web_backend.py | Initializes trading runtime | Async fragmentation |
| app.py | Initializes websocket runtime | Detached websocket lineage |
| mcp_trading_server.py | Starts MCP orchestration | Distributed runtime authority |

---

## Broker Execution Entry Points

| Component | File | Execution Authority | Canonical |
|---|---|---|---|
| ExecutionTool | backend/hft2/backend/mcp_server/tools/execution_tool.py | Trade orchestration | YES |
| LiveTradingExecutor | backend/hft2/backend/live_executor.py | Canonical execution engine | YES |
| dhan_client.py | backend/hft2/backend/dhan_client.py | Broker execution | YES |
| broker_adapter.py | backend/hft2/backend/broker_adapter.py | Broker abstraction | PARTIAL |
| simulator.py | backend/hft2/backend/hft/shadow_execution/simulator.py | Shadow execution | NO |

---

## Async Runtime Entry Points

| Component | Async Type | Replay Safe | Trace Safe |
|---|---|---|---|
| enhanced_websocket_manager.py | WebSocket Manager | PARTIAL | PARTIAL |
| async_signal_collector.py | Async signal collection | PARTIAL | PARTIAL |
| web_backend.py | SSE + async runtime | PARTIAL | PARTIAL |
| tracker_agent.py | Background monitoring threads | NO | PARTIAL |
| api_server.py | Background prediction threads | PARTIAL | PARTIAL |

---

## Hidden Runtime Paths

| Component | Risk |
|---|---|
| simple_app.py | Secondary runtime authority |
| simulator.py | Mock execution ambiguity |
| verify_hft.py | Non-canonical replay behavior |
| testindia.py | Massive runtime mutation surface |
| shadow_execution/ | Detached execution semantics |

---

## Initial Convergence Findings

- Runtime topology remains partially fragmented.
- Multiple runtime authorities still exist.
- Async execution regions are highly distributed.
- Trace lineage is not yet canonicalized.
- Replay persistence remains partially fragmented.
- Broker acknowledgement replay continuity remains incomplete.