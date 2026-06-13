# EXECUTION_AUTHORITY_REPORT.md

## Current Execution Paths

### Path 1 — Canonical Production Execution Path

```text
Web/API
    ↓
ExecutionTool
    ↓
LiveTradingExecutor
    ↓
DhanAPIClient
    ↓
Broker
```

Evidence gathered from:

* backend/hft2/backend/mcp_server/tools/execution_tool.py
* backend/hft2/backend/web_backend.py
* backend/hft2/backend/live_executor.py

Observed execution calls:

```python
live_executor.place_order(...)
```

and

```python
self.live_executor.place_order(...)
```

This path is currently the primary production execution path.

---

### Path 2 — Request Context Execution Path

```text
request_context
    ↓
broker_adapter
    ↓
dhan_client.place_order_market
    ↓
Broker
```

Evidence gathered from:

* backend/hft2/backend/request_context.py
* backend/hft2/backend/broker_adapter.py

Repository analysis showed this path bypasses LiveTradingExecutor.

Repository analysis did not identify active runtime callers.

---

## Canonical Execution Path

Canonical execution authority:

```text
Web/API
    ↓
ExecutionTool
    ↓
LiveTradingExecutor
    ↓
DhanAPIClient
    ↓
Broker
```

ExecutionTool acts as orchestration.

LiveTradingExecutor acts as execution authority.

DhanAPIClient acts as broker communication layer.

All production execution should route through this execution spine.

---

## Deprecated Execution Paths

### Deprecated Path

```text
request_context
    ↓
broker_adapter
    ↓
dhan_client
```

Reason for deprecation:

* bypasses LiveTradingExecutor
* creates execution ownership ambiguity
* introduces potential future authority drift

Implementation completed:

```python
place_order_for_request_user(...)
```

now raises:

```python
RuntimeError(
    "Deprecated execution path. All order execution must route through LiveTradingExecutor."
)
```

---

## Migration Strategy

Execution ownership is consolidated around LiveTradingExecutor.

Actions performed:

1. Identified broker execution bypass path.
2. Verified no active callers for place_order_for_request_user().
3. Deprecated direct execution through request_context.
4. Added convergence protection preventing future use of the deprecated path.

Surviving execution routes:

```text
Web/API
    ↓
LiveTradingExecutor
```

```text
ExecutionTool
    ↓
LiveTradingExecutor
```

No additional execution routes were proven during this phase.

---

## Final Ownership Declaration

Execution Authority Owner:

```text
LiveTradingExecutor
```

ExecutionTool:

```text
Orchestration only
```

DhanAPIClient:

```text
Broker communication only
```

request_context:

```text
Portfolio context only
```

Direct broker execution outside LiveTradingExecutor is deprecated.

Target authority model:

```text
One Execution Authority
=
LiveTradingExecutor
```

---

## Implementation Deliverables

### Remove execution bypasses where appropriate

Status: Completed

Deprecated:

```text
request_context
    ↓
broker_adapter
    ↓
dhan_client
```

### Prevent direct broker routing outside canonical path

Status: Completed

Added RuntimeError protection in:

```text
backend/hft2/backend/request_context.py
```

### Document all surviving execution routes

Status: Completed

Surviving routes:

```text
Web/API → LiveTradingExecutor
ExecutionTool → LiveTradingExecutor
```

### Produce runtime proof

Status: Pending

Current blocker:

```text
Runtime environment not operational.
FastAPI dependency missing in local environment.
```

Runtime execution validation will be completed after environment startup validation.

---

## Success Condition Assessment

Required:

```text
Every execution request reaches broker through one canonical execution spine.
```

Current Assessment:

Partially Proven

Proven:

* Production execution routes through LiveTradingExecutor.
* Deprecated execution bypass identified and blocked.

Not Yet Proven:

* End-to-end runtime validation.
* Live broker execution proof.
* Runtime trace showing execution request reaching broker through canonical spine.

Additional runtime validation required before full completion can be declared.
