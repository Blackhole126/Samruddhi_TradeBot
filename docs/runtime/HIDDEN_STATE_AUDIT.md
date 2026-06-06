# Hidden State Audit

## Hidden Runtime State Regions

| Region | Risk |
|---|---|
| active_connections websocket lists | Runtime-only state |
| _portfolio_histories memory snapshots | Replay discontinuity |
| SSE snapshot generation | Detached runtime truth |
| cache persistence layers | Stale execution state |
| threading locks/events | Hidden execution synchronization |
| shadow execution state | Non-canonical execution truth |

---

## Hidden State Findings

- Significant runtime truth still exists in memory-only regions.
- WebSocket runtime state is not fully replay-safe.
- SSE state propagation introduces detached observability risk.
- Cache layers may introduce stale execution visibility.
- Shadow execution state coexists with live runtime state.