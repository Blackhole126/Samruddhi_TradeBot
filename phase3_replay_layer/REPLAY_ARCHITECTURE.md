# REPLAY_ARCHITECTURE.md

# Replay-Safe Execution Architecture

## Objective

Validate replay-safe execution foundations across:
- prediction lifecycle
- execution lifecycle
- portfolio persistence
- audit persistence
- observability lineage

---

# 1. REPLAY FOUNDATIONS IDENTIFIED

Validated replay-capable systems:

| Component | Replay Capability |
|---|---|
| MCP request logs | request replay |
| MCP response logs | response replay |
| integration_audit.db | execution reconstruction |
| integration_audit.jsonl | immutable event logging |
| DecisionAuditTrail | decision lineage |
| feature_snapshot | feature replay |
| portfolio_snapshot | portfolio reconstruction |
| created_at timestamps | deterministic ordering |
| request_id propagation | lineage continuity |

---

# 2. REQUEST LINEAGE PERSISTENCE

Validated:
- request_id propagation exists across:
  - API layer
  - MCP adapter
  - audit persistence
  - response persistence
  - integration logs

Observed files:
- backend/data/logs/mcp_requests/
- backend/data/logs/integration_audit.jsonl
- integration_audit.db

Request lineage continuity is strongly implemented.

---

# 3. IMMUTABLE EXECUTION LOGGING

Observed append-style replay logs:

- mcp_requests/*.jsonl
- mcp_responses/*.jsonl
- integration_audit.jsonl

Properties:
- append-oriented
- timestamped
- request-linked
- replay-capable

These form primitive immutable replay streams.

---

# 4. DETERMINISTIC EVENT ORDERING

Validated ordering mechanisms:

| Mechanism | Status |
|---|---|
| timestamp | present |
| created_at | present |
| request_id | present |
| DB insertion ordering | present |

Replay ordering is partially deterministic.

However:
- no global sequence_id architecture exists
- detached async execution may weaken strict ordering guarantees

---

# 5. REPLAY SNAPSHOT SYSTEMS

Replay-oriented snapshots identified:

| Snapshot Type | Location |
|---|---|
| feature_snapshot | stock_analysis_complete.py |
| portfolio_snapshot | portfolio_tool.py |
| SSE bot snapshot | web_backend.py |
| order book snapshots | hft/microstructure |

Replay reconstruction capability exists partially.

---

# 6. AUDIT TRAIL ARCHITECTURE

Strong audit persistence identified:

- DecisionAuditTrail
- integration_audit.db
- integration_audit.jsonl

Persisted fields include:
- request_id
- timestamp
- endpoint
- symbol
- quantity
- execution metadata
- success/failure state

This significantly improves replay reconstruction capability.

---

# 7. REPLAY-SAFE GAPS

Critical replay risks still exist:

| Risk | Impact |
|---|---|
| pending_orders in memory | replay loss |
| active_orders transient state | incomplete reconstruction |
| detached asyncio tasks | lineage discontinuity |
| mutable caches | non-deterministic replay |
| missing sequence_id | partial ordering ambiguity |

---

# 8. RECONSTRUCTION CAPABILITY STATUS

Current capability:

| Reconstruction Type | Status |
|---|---|
| API replay | Strong |
| prediction replay | Strong |
| request lineage replay | Strong |
| audit replay | Strong |
| portfolio replay | Partial |
| execution replay | Partial |
| async replay continuity | Incomplete |

---

# 9. CONCLUSION

The system already contains strong replay-safe architectural foundations through:
- structured request persistence
- audit logging
- immutable JSONL streams
- timestamped event persistence
- request lineage continuity

However:
- full event sourcing architecture is not yet implemented
- transient runtime state still exists
- strict deterministic replay guarantees remain incomplete

The platform is structurally capable of partial replay reconstruction and deterministic audit validation.