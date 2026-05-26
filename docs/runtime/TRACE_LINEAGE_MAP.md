# Trace Lineage Map

## Current Runtime Identifiers

| Identifier | Location | Purpose |
|---|---|---|
| request_id | api_server.py | API request tracking |
| session_id | app.py / MCP server | Session tracking |
| tracking_id | decision_audit_trail.py | Decision lineage |
| decision_id | decision_audit_trail.py | Audit persistence |
| job_id | api_server.py | Prediction job tracking |

---

## Major Finding

No globally canonical trace_id currently exists across the full runtime spine.

Current lineage is fragmented across:
- request_id
- session_id
- tracking_id
- decision_id
- broker execution identifiers

---

## Trace Fragmentation Regions

| Region | Risk |
|---|---|
| Async execution tasks | Detached lineage |
| WebSocket runtime | Trace discontinuity |
| SSE runtime | Partial trace propagation |
| Replay reconstruction | Incomplete lineage continuity |
| Broker acknowledgement | External lineage gap |

---

## Convergence Requirement

Future convergence phases must unify:
- request lineage
- execution lineage
- replay lineage
- broker lineage
- observability lineage

into:
→ one canonical trace_id propagation model.