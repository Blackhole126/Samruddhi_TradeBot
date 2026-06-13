# REPLAY_AUTHORITY_REPORT.md

## Objective

Establish a single replay authority, reduce replay ownership fragmentation, and move Samruddhi toward a deterministic replay-safe execution model.

---

# Replay Entry Point

## Previous State

Replay persistence infrastructure existed within the replay subsystem:

```text
ReplayEvent
ReplayStore
ReplayValidator
```

However, repository investigation identified no active execution path generating replay events.

Replay persistence existed but replay ownership was fragmented and not connected to the canonical execution flow.

---

## Canonical Replay Entry Point

Replay authority is now established at:

```text
LiveTradingExecutor
```

All execution outcomes are expected to generate replay events through the canonical execution authority.

Canonical flow:

```text
LiveTradingExecutor
        ↓
ReplayEvent
        ↓
persist_replay_event()
        ↓
ReplayStore
        ↓
ReplayValidator
```

---

# Replay Schema

Replay events use the ReplayEvent structure.

Current schema:

```python
ReplayEvent(
    schema_version,
    request_id,
    trace_id,
    timestamp_utc,
    event_type,
    source,
    payload
)
```

Fields:

| Field          | Purpose                     |
| -------------- | --------------------------- |
| schema_version | Replay schema version       |
| request_id     | Replay request identifier   |
| trace_id       | Replay lineage identifier   |
| timestamp_utc  | Canonical UTC timestamp     |
| event_type     | Replay event classification |
| source         | Replay event producer       |
| payload        | Execution metadata          |

Timestamp generation uses:

```python
utc_iso()
```

from:

```text
backend/core/time_utils.py
```

ensuring UTC normalization.

---

# Replay Ownership

## Previous State

Replay persistence functionality existed:

```python
persist_replay_event()
```

However repository investigation showed no execution authority generating replay events.

Replay ownership was therefore fragmented and unproven.

---

## Current State

Replay ownership is assigned to:

```text
LiveTradingExecutor
```

Implementation added replay generation for:

### Successful Buy Orders

```text
TRADE_EXECUTED
```

### Successful Sell Orders

```text
TRADE_EXECUTED
```

### Failed Buy Orders

```text
TRADE_FAILED
```

### Failed Sell Orders

```text
TRADE_FAILED
```

Canonical ownership model:

```text
LiveTradingExecutor
        ↓
ReplayEvent
        ↓
persist_replay_event()
        ↓
ReplayStore
```

No additional replay authorities were identified during this phase.

---

# Replay Lifecycle

Current replay lifecycle:

```text
Execution Request
        ↓
LiveTradingExecutor
        ↓
Execution Result
        ↓
ReplayEvent
        ↓
persist_replay_event()
        ↓
ReplayStore
        ↓
replay_snapshots/<trace_id>.jsonl
        ↓
ReplayValidator
```

Replay persistence stores events using trace-scoped replay files.

Each replay file contains an ordered sequence of replay events.

Replay ordering is validated through:

```python
validate_replay_sequence()
```

located in:

```text
backend/replay/replay_validator.py
```

---

# Replay Reconstruction Process

Replay reconstruction is trace-based.

Reconstruction flow:

```text
trace_id
        ↓
replay_snapshots/<trace_id>.jsonl
        ↓
Replay Event Sequence
        ↓
Replay Validation
        ↓
Execution Reconstruction
```

Each replay file represents a replay lineage associated with a specific trace.

Replay reconstruction supports:

### Successful Trade Reconstruction

```text
TRADE_EXECUTED
```

events persisted through ReplayStore.

### Failed Trade Reconstruction

```text
TRADE_FAILED
```

events persisted through ReplayStore.

### Replay Lineage Tracking

```text
trace_id
```

acts as the canonical replay lineage identifier.

---

# Implementation Deliverables

## Establish Canonical Replay Source

Status:

```text
Completed
```

Canonical replay authority:

```text
LiveTradingExecutor
```

---

## Route Replay Persistence Through Canonical Authority

Status:

```text
Completed
```

Implementation added replay generation within:

```text
backend/hft2/backend/live_executor.py
```

Replay events are now persisted through:

```python
persist_replay_event()
```

---

## Validate Reconstruction Path

Status:

```text
Partially Validated
```

Repository validation confirmed:

```text
ReplayEvent
        ↓
ReplayStore
        ↓
ReplayValidator
```

and trace-based replay persistence.

Runtime reconstruction validation remains pending environment startup validation.

---

## Generate Runtime Proof

Status:

```text
Pending
```

Current blocker:

```text
Local runtime environment not operational.
FastAPI dependencies not yet installed and validated.
```

Runtime replay validation will be completed during Production Readiness and Joint Validation phases.

---

# Success Condition Assessment

## A Successful Trade Can Be Reconstructed

Status:

```text
Implemented
```

Successful execution paths generate:

```text
TRADE_EXECUTED
```

replay events.

---

## A Failed Trade Can Be Reconstructed

Status:

```text
Implemented
```

Failure execution paths generate:

```text
TRADE_FAILED
```

replay events.

---

## A Replay Lineage Can Be Followed

Status:

```text
Implemented
```

Replay lineage is organized using:

```text
trace_id
```

and persisted within:

```text
replay_snapshots/<trace_id>.jsonl
```

---

# Final Replay Authority Declaration

Replay Authority Owner:

```text
LiveTradingExecutor
```

Replay Persistence Authority:

```text
ReplayStore
```

Replay Validation Authority:

```text
ReplayValidator
```

Canonical Replay Spine:

```text
LiveTradingExecutor
        ↓
ReplayEvent
        ↓
persist_replay_event()
        ↓
ReplayStore
        ↓
ReplayValidator
```

This phase materially reduces replay ownership fragmentation and moves Samruddhi closer to a single replay authority model.
