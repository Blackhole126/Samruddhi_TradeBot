# EXECUTION OWNERSHIP MAP

## Phase
Phase 1 — Full Repo Acquisition + System Surface Mapping

---

# Objective

Identify and map:

- execution authority regions
- orchestration ownership
- broker ownership
- replay ownership
- portfolio ownership
- runtime enforcement layers
- execution lifecycle topology

---

# Canonical Execution Lifecycle

Current observed execution flow:

Signal
→ MCP Adapter
→ Execution Tool
→ Broker Adapter
→ Live Executor
→ Broker Layer
→ Portfolio Synchronization
→ Replay/Audit
→ Observability

Current State:
Execution convergence direction exists but execution authority remains partially distributed.

---

# Execution Ownership Regions

## API Execution Layer

Detected:
- api_server.py
- web_backend.py
- routes.py

Responsibilities:
- external execution requests
- request validation
- runtime exposure
- execution triggering

---

## MCP Execution Layer

Detected:
- execution_tool.py
- mcp_adapter.py
- mcp_service/

Responsibilities:
- execution orchestration
- tool routing
- execution coordination
- agent-linked execution control

Current Finding:
Execution orchestration partially duplicated across runtime regions.

---

## Broker Abstraction Layer

Detected:
- broker_adapter.py

Responsibilities:
- broker abstraction
- broker registration
- execution routing
- execution normalization

Positive Signal:
Canonical broker abstraction direction operationally exists.

---

## Live Execution Layer

Detected:
- live_executor.py
- dhan_client.py
- fyers_client.py

Responsibilities:
- live order placement
- broker communication
- market execution
- portfolio synchronization

---

## HFT Execution Layer

Detected:
- execution_router.py
- hft pipeline
- tick engine
- microstructure runtime

Responsibilities:
- HFT execution routing
- tick-driven execution
- slippage-aware execution
- shadow execution integration

Current Finding:
HFT execution lifecycle still partially separate from canonical execution path.

---

## Shadow Execution Layer

Detected:
- shadow_execution/simulator.py
- trade_state_machine.py

Responsibilities:
- replay-safe execution simulation
- execution validation
- execution reconstruction
- safe-mode execution flow

Positive Signal:
Safe-mode vs live-mode separation operationally exists.

---

# Portfolio Ownership Regions

Detected:
- portfolio_manager.py
- portfolio synchronization systems
- broker-linked portfolio retrieval

Responsibilities:
- portfolio state tracking
- broker synchronization
- execution truth persistence
- runtime portfolio continuity

---

# Replay Ownership Regions

Detected:
- DecisionAuditTrail
- replay_store.py
- replay_validator.py
- audit persistence systems

Responsibilities:
- decision lineage
- replay continuity
- audit reconstruction
- execution replay tracking

Current Finding:
Replay-awareness integrated but globally singular replay authority not fully proven.

---

# Observability Ownership Regions

Detected:
- production_monitor.py
- performance_monitor.py
- failure_tracker.py
- structured logging regions

Responsibilities:
- execution visibility
- runtime diagnostics
- failure visibility
- runtime monitoring

Current Finding:
Observability operationally integrated but globally unified trace continuity remains partial.

---

# Major Execution Risks

## Distributed Execution Authority
Execution ownership spans multiple runtime regions.

---

## Multiple Execution Entrypoints
Execution may be triggered through:
- API runtime
- MCP runtime
- HFT runtime
- web backend runtime

---

## Replay Divergence Risk
Replay continuity distributed across:
- execution systems
- reasoning systems
- persistence systems

---

## HFT Runtime Separation
HFT runtime still partially independent from canonical execution lifecycle.

---

## Runtime Orchestration Duplication
mcp_service and mcp_server overlap orchestration responsibilities.

---

# Positive Convergence Signals

- broker abstraction operationally exists
- live vs shadow execution separation exists
- replay-aware execution exists
- runtime safety layers exist
- portfolio synchronization exists
- execution lifecycle modularization exists

---

# Conclusion

Execution ownership acquisition successfully mapped the operational execution lifecycle of Samruddhi.

The platform demonstrates:
- strong execution maturity progression
- broker abstraction evolution
- replay-aware execution design
- live/shadow execution separation
- portfolio-linked execution continuity

However:
- execution authority remains partially distributed
- orchestration convergence remains incomplete
- replay convergence remains partial
- HFT runtime convergence remains incomplete

Further canonicalization is required to achieve one singular execution authority spine across the platform.