# Timezone Audit

## Current Timestamp Implementations

| Pattern | Runtime Region | UTC Safe |
|---|---|---|
| datetime.now() | MCP adapter + runtime systems | NO |
| datetime.utcnow() | DB + commodities | PARTIAL |
| timezone.utc | Samachar ingestion | YES |
| Asia/Kolkata timezone | execution runtime | PARTIAL |
| naive isoformat() | MCP adapter | NO |

---

## Major Convergence Finding

The runtime currently contains mixed timezone semantics across:
- naive local datetimes
- utcnow()
- timezone.utc
- Asia/Kolkata localized timestamps

This creates:
- replay ordering ambiguity
- cross-runtime sequencing inconsistency
- async replay continuity risk
- broker reconciliation ambiguity

---

## Highest-Risk Runtime Regions

| File | Risk |
|---|---|
| core/mcp_adapter.py | naive datetime.now().isoformat() |
| execution_tool.py | mixed IST/local handling |
| decision_audit_trail.py | naive datetime persistence |
| async_signal_collector.py | async timestamp ambiguity |

---

## Positive Convergence Signals

Samachar ingestion pipeline already demonstrates proper UTC normalization using:
- timezone.utc
- astimezone(timezone.utc)
- ISO UTC serialization

This provides a strong reference implementation for canonical runtime convergence.

---

## Required Convergence Actions

Phase 2 established the canonical timezone normalization standard and enforcement utilities.

Full runtime migration of all naive datetime regions was intentionally deferred to later replay-safe convergence phases to avoid:

- replay chronology corruption
- async runtime instability
- broker synchronization drift
- pandas timezone regression
- deterministic ordering divergence

Future convergence phases will progressively integrate:
- canonical UTC persistence
- replay-safe timestamp normalization
- unified async chronology
- deterministic runtime ordering