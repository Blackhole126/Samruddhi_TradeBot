# FRAGMENTATION_REPORT.md

# Samruddhi Canonical Execution Spine Audit

## Phase 4 – Fragmentation Detection Report

---

# Objective

Identify all execution islands, duplicate ownership regions, fragmented runtime paths, and competing authorities that prevent Samruddhi from operating as one deterministic execution organism.

Audit Scope:

* Duplicate Validation
* Duplicate Persistence
* Duplicate Tracing
* Duplicate Observability
* Duplicate Contract Ownership
* Duplicate Execution Paths

---

# Executive Summary

This audit identified multiple fragmentation regions across the Samruddhi ecosystem.

Execution authority has undergone significant convergence toward the ExecutionTool → LiveTradingExecutor model.

However, repository evidence demonstrates that several parallel systems still exist for execution, validation, tracing, observability, persistence, and contract management.

The most critical finding is the existence of a direct broker execution path that bypasses the canonical execution spine.

Current Conclusion:

Samruddhi is not yet operating as a fully converged deterministic execution organism.

Multiple execution-adjacent islands remain active within the repository.

---

# Fragmentation Issue 1

## Duplicate Execution Paths

### Location

Canonical Execution Path

* backend/hft2/backend/mcp_server/tools/execution_tool.py
* backend/hft2/backend/live_executor.py
* backend/hft2/backend/web_backend.py

Direct Broker Execution Path

* backend/hft2/backend/request_context.py
* backend/hft2/backend/broker_adapter.py
* backend/hft2/backend/dhan_client.py

### Evidence

Canonical Path:

ExecutionTool
→ LiveTradingExecutor
→ Dhan

Repository comments explicitly state:

* ExecutionTool delegates to LiveTradingExecutor
* LiveTradingExecutor is the execution engine

Direct Path:

request_context.py contains:

place_order_for_request_user()

which imports:

broker_adapter.place_order()

which directly invokes:

dhan_client.place_order_market()

This path bypasses:

* ExecutionTool
* LiveTradingExecutor
* Canonical execution orchestration

### Impact

Execution authority is not fully centralized.

Orders may potentially reach the broker through multiple execution paths.

### Risk

HIGH

Execution drift.

Replay inconsistency.

Observability inconsistency.

Authority ambiguity.

### Recommended Resolution

Enforce a single execution authority:

ExecutionTool
→ LiveTradingExecutor
→ Broker

Remove or explicitly classify direct broker execution routes.

---

# Fragmentation Issue 2

## Duplicate Validation Authorities

### Location

Validation systems identified:

* backend/validators.py
* backend/core/schema_validator.py
* backend/samachar/contract_validator.py
* backend/hft2/backend/config/config_schema.py
* backend/hft2/backend/utils/validators.py
* MCP argument validation
* Pydantic validators inside api_server.py

### Evidence

Repository contains multiple independent validation frameworks.

Each validates different runtime regions.

No unified validation authority was identified.

### Impact

Validation behavior may diverge between subsystems.

### Risk

MEDIUM

Contract inconsistency.

Runtime drift.

Validation rule duplication.

### Recommended Resolution

Create a validation ownership matrix.

Define:

* API validation authority
* Contract validation authority
* Configuration validation authority
* Execution validation authority

---

# Fragmentation Issue 3

## Duplicate Persistence Authorities

### Location

Replay Persistence

* backend/replay/replay_store.py

Observability Persistence

* backend/observability/observability_store.py

Audit Persistence

* backend/integration_audit.py

Portfolio Persistence

* portfolio_positions table
* IntegrationAuditStore database

### Evidence

Repository contains multiple independent persistence mechanisms.

Replay data, observability data, audit data, and portfolio data are stored separately.

### Impact

Execution truth becomes distributed across multiple persistence layers.

### Risk

HIGH

Difficult reconstruction.

State divergence.

Conflicting historical records.

### Recommended Resolution

Define persistence ownership:

Execution Truth Source

Replay Truth Source

Observability Truth Source

Portfolio Truth Source

---

# Fragmentation Issue 4

## Duplicate Tracing Authorities

### Location

Trace usage identified in:

* execution_contract.py
* replay_event.py
* observability_event.py
* failure_tracker.py
* portfolio_visibility.py

### Evidence

trace_id appears across multiple systems.

No single trace generation authority was identified.

Multiple systems consume trace_id.

Trace propagation ownership is not documented.

### Impact

Lineage continuity cannot be guaranteed across all runtime regions.

### Risk

HIGH

Broken reconstruction.

Incomplete audit trails.

Trace discontinuity.

### Recommended Resolution

Establish a canonical trace authority.

Every runtime region should inherit lineage from one trace source.

---

# Fragmentation Issue 5

## Duplicate Observability Systems

### Location

Observability Layer

* observability_store.py
* observability_event.py
* failure_tracker.py

Monitoring Layer

* logging_utils.py
* production_monitor.py

Audit Layer

* integration_audit.py

### Evidence

Repository contains multiple independent visibility systems.

Observability events.

Failure events.

Structured logs.

Production monitoring.

Audit persistence.

All operate separately.

### Impact

System visibility becomes fragmented.

### Risk

MEDIUM

Operators may need multiple systems to understand failures.

### Recommended Resolution

Create a canonical observability topology.

Define:

Event Source

Persistence Layer

Monitoring Layer

Operator Visibility Layer

---

# Fragmentation Issue 6

## Duplicate Contract Ownership

### Location

Canonical Contract Layer

* execution_contract.py
* schema_validator.py

Replay Contract Layer

* replay_event.py

Observability Contract Layer

* observability_event.py

Failure Contract Layer

* failure_tracker.py

Samachar Contract Layer

* samachar/contract_validator.py

### Evidence

Multiple schema definitions exist.

Execution contracts use:

* schema_version
* request_id
* trace_id
* timestamp_utc

Failure contracts maintain their own schema version.

Replay and observability maintain separate event contracts.

Samachar maintains independent contract validation.

### Impact

Contract ownership is distributed.

Schema evolution may diverge.

### Risk

HIGH

Contract drift.

Lineage inconsistency.

Replay incompatibility.

### Recommended Resolution

Create one canonical contract authority.

All runtime events should inherit:

* schema_version
* request_id
* trace_id
* timestamp_utc
* provenance

---

# Fragmentation Issue 7

## Runtime Entry Point Fragmentation

### Location

FastAPI applications discovered:

* backend/api_server.py
* backend/api_wrapper.py
* backend/hft2/backend/app.py
* backend/hft2/backend/simple_app.py
* backend/hft2/backend/web_backend.py
* backend/hft2/mcp_service/api_server.py
* backend/samachar/api_server.py

### Evidence

Seven FastAPI runtime entry points were identified.

### Impact

Runtime topology is not fully consolidated.

### Risk

MEDIUM

Deployment ambiguity.

Ownership ambiguity.

Operational complexity.

### Recommended Resolution

Document:

Production Entry Point

Secondary Services

Testing Services

Deprecated Services

---

# Fragmentation Severity Summary

| Fragmentation Area                | Severity |
| --------------------------------- | -------- |
| Duplicate Execution Paths         | HIGH     |
| Duplicate Validation Authorities  | MEDIUM   |
| Duplicate Persistence Authorities | HIGH     |
| Duplicate Tracing Authorities     | HIGH     |
| Duplicate Observability Systems   | MEDIUM   |
| Duplicate Contract Ownership      | HIGH     |
| Runtime Entry Point Fragmentation | MEDIUM   |

---

# Final Assessment

The audit identified multiple execution-adjacent fragmentation regions.

Most critical findings:

1. Direct broker execution path bypasses canonical execution spine.
2. Multiple persistence authorities exist.
3. Multiple tracing authorities exist.
4. Multiple contract systems exist.
5. Runtime topology remains fragmented.

Current State:

Samruddhi demonstrates substantial convergence progress.

However, repository evidence does not support the conclusion that the platform currently operates as a fully unified deterministic execution organism.

Additional convergence work remains necessary before that claim can be validated.
