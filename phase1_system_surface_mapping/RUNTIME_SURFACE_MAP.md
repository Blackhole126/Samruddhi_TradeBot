# RUNTIME SURFACE MAP

## Phase
Phase 1 — Full Repo Acquisition + System Surface Mapping

---

# Objective

Acquire, run, map, and understand the complete Samruddhi platform runtime surface across:

- stock runtime systems
- crypto runtime systems
- commodity runtime systems
- replay systems
- observability systems
- deployment systems
- broker/exchange layers
- ingestion systems
- execution systems
- portfolio systems
- deployment topology

---

# Runtime Entrypoints Identified

## Primary API Runtime

- backend/api_server.py
- backend/api_wrapper.py

Purpose:
Primary FastAPI gateway and runtime orchestration entry surface.

---

## HFT Runtime

- backend/hft2/backend/app.py
- backend/hft2/backend/web_backend.py

Purpose:
HFT runtime execution, web runtime integration, execution routing, broker-linked runtime operations.

---

## MCP Runtime

- backend/core/mcp_adapter.py
- backend/hft2/backend/mcp_server/
- backend/mcp_service/

Purpose:
Runtime orchestration, tool routing, execution coordination, multi-agent integration.

---

## Samachar Runtime

- backend/samachar/api_server.py

Purpose:
News ingestion, intelligence acquisition, sentiment/runtime data ingestion.

---

# Multi-Market Runtime Regions

## Stock Runtime

Detected Components:
- Dhan execution
- Fyers integration
- NSE/BSE exchange handling
- live execution routing
- portfolio synchronization
- prediction lifecycle

---

## Crypto Runtime

Detected Components:
- ccxt integrations
- exchange abstractions
- websocket-linked exchange handling
- crypto execution tooling

---

## Commodity Runtime

Detected Components:
- commodity ingestion
- signal generation
- exchange-linked abstractions
- runtime feature engineering

---

# Replay Runtime Regions

Detected Components:
- replay/
- replay_store.py
- replay_validator.py
- trade_state_machine.py
- DecisionAuditTrail

Current State:
Replay-awareness operationally integrated but canonical immutable replay spine not fully proven.

---

# Observability Runtime Regions

Detected Components:
- observability/
- failure_tracker.py
- production_monitor.py
- performance_monitor.py
- structured logging regions

Current State:
Strong runtime visibility exists but globally unified trace-aware observability spine remains partial.

---

# Deployment Runtime Regions

Detected Components:
- docker-compose.yml
- render.yaml
- render_start.sh
- deployment/
- runtime.txt

Current State:
Deployment preparation present but unified deployment convergence still partial.

---

# Runtime Convergence Findings

## Positive Signals

- broker abstraction direction exists
- replay-awareness integrated
- structured logging operational
- live vs shadow execution separation exists
- runtime safety layers exist
- environment-driven deployment structure exists

---

## Major Runtime Risks

### Runtime Fragmentation
Multiple runtime entrypoints still exist.

### Orchestration Duplication
mcp_service and mcp_server both exist as orchestration regions.

### Distributed Execution Authority
Execution ownership still distributed across multiple runtime layers.

### Replay Divergence Risk
Replay state distributed across execution, reasoning, and persistence layers.

### Observability Divergence Risk
Observability exists broadly but unified trace continuity remains partial.

---

# Conclusion

Phase 1 runtime acquisition successfully identified the complete operational runtime surface of Samruddhi.

Runtime mapping confirmed:
- multi-market runtime architecture
- broker-linked execution systems
- replay-aware runtime behavior
- observability integration
- deployment topology regions
- orchestration fragmentation regions
- canonical convergence direction

The platform demonstrates strong convergence maturity progression but still contains partially fragmented runtime authority regions requiring future canonicalization work.