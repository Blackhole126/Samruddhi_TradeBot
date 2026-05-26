# Observability Region Map

## Observability Regions

| Region | Observable | Replayable |
|---|---|---|
| API runtime | YES | PARTIAL |
| Execution runtime | YES | PARTIAL |
| Broker runtime | PARTIAL | PARTIAL |
| WebSocket runtime | PARTIAL | NO |
| SSE runtime | PARTIAL | NO |
| Decision audit trail | YES | YES |
| Shadow execution | PARTIAL | PARTIAL |

---

## Observability Findings

- Structured logging maturity has improved significantly.
- Audit trail infrastructure exists.
- Replay observability remains partially fragmented.
- Async runtime observability continuity remains incomplete.
- Broker truth visibility is not yet fully canonicalized.