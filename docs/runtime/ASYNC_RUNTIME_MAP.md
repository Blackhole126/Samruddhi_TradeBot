# Async Runtime Map

## Async Execution Regions

| Component | Async Type | Risk |
|---|---|---|
| enhanced_websocket_manager.py | WebSocket async runtime | Detached lineage |
| async_signal_collector.py | Async signal gathering | Replay fragmentation |
| decision_audit_trail.py | Async persistence | Ordering ambiguity |
| web_backend.py | SSE async runtime | Observability fragmentation |
| tracker_agent.py | Background monitoring threads | Non-deterministic behavior |
| api_server.py | Prediction worker threads | Distributed execution state |

---

## Concurrency Findings

- Runtime contains extensive async orchestration.
- Multiple threading regions exist simultaneously.
- Deterministic execution ordering is not globally guaranteed.
- Async replay continuity remains partially incomplete.
- Observability continuity across async boundaries remains fragmented.