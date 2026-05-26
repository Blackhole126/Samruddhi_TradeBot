# Contract Fragmentation Analysis

## Current Runtime Identifier Sources

| Identifier | Primary File | Purpose | Canonical Status |
|---|---|---|---|
| request_id | core/mcp_adapter.py | request lineage | PARTIAL |
| session_id | MCP runtime + websocket runtime | session tracking | PARTIAL |
| tracking_id | decision_audit_trail.py | performance lineage | PARTIAL |
| decision_id | decision_audit_trail.py | audit persistence | PARTIAL |
| job_id | api_server.py | async prediction tracking | PARTIAL |

---

## Major Runtime Finding

backend/core/mcp_adapter.py currently behaves as the closest implementation of a canonical runtime execution spine.

Current capabilities:
- request lineage propagation
- execution orchestration
- runtime coordination
- partial observability continuity

However:
runtime-wide canonical trace propagation does not yet exist.

---

## Current Fragmentation Risks

| Region | Risk |
|---|---|
| request lineage | fragmented propagation |
| session lineage | subsystem-local semantics |
| async execution | detached correlation |
| replay reconstruction | incomplete lineage continuity |
| broker execution | non-canonical trace continuity |

---

## Missing Canonical Runtime Fields

- trace_id
- schema_version
- timestamp_utc
- provenance metadata

---

## Convergence Requirement

Future runtime convergence must unify:
- request lineage
- replay lineage
- broker lineage
- observability lineage
- async propagation lineage

into:
→ one canonical execution contract structure.