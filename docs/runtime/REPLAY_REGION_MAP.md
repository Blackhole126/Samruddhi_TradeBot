# Replay Region Map

## Replay Persistence Regions

| Region | Persistence Type | Replay Safe |
|---|---|---|
| decision_audit_trail.py | Audit file persistence | PARTIAL |
| samruddhi_memory.py | Database persistence | PARTIAL |
| SSE snapshots | In-memory snapshots | NO |
| portfolio snapshots | Rolling memory snapshots | PARTIAL |
| monitoring logs | File persistence | YES |
| shadow_execution simulator | Shadow replay | PARTIAL |

---

## Replay Risk Regions

| Region | Risk |
|---|---|
| WebSocket state | Non-persistent |
| SSE snapshots | Detached replay continuity |
| Background threads | Non-deterministic replay |
| Cache persistence | Mutable replay state |
| Async execution tasks | Ordering ambiguity |

---

## Major Replay Findings

- Replay architecture exists but remains partially fragmented.
- Immutable replay persistence is not yet globally enforced.
- Replay continuity across async boundaries is incomplete.
- Broker-confirmed replay reconstruction remains incomplete.