# REPO TOPOLOGY MAP

## Phase
Phase 1 — Full Repo Acquisition + System Surface Mapping

---

# Objective

Map the complete repository topology and identify:

- runtime ownership regions
- deployment regions
- replay regions
- observability regions
- broker/exchange regions
- orchestration regions
- ingestion regions
- execution regions
- portfolio lifecycle regions

---

# High-Level Repository Structure

## Backend Runtime Layer

Primary Region:
- backend/

Purpose:
Core runtime execution surface for:
- API orchestration
- prediction runtime
- execution runtime
- replay systems
- observability systems
- broker integrations
- HFT runtime
- MCP runtime

---

# Runtime Topology Regions

## API Runtime Region

Detected:
- api_server.py
- api_wrapper.py
- web_backend.py
- app.py

Responsibilities:
- FastAPI runtime exposure
- request routing
- runtime orchestration
- websocket coordination
- execution trigger surfaces

---

## MCP Runtime Region

Detected:
- core/mcp_adapter.py
- mcp_service/
- hft2/backend/mcp_server/

Responsibilities:
- tool orchestration
- multi-agent coordination
- execution routing
- prediction coordination
- portfolio interaction

Current Finding:
Multiple MCP orchestration regions exist.

Potential Risk:
- orchestration duplication
- onboarding ambiguity
- runtime divergence

---

## HFT Runtime Region

Detected:
- hft2/backend/hft/

Subregions:
- intraday/
- microstructure/
- reporting/
- risk/
- shadow_execution/
- tick_engine/

Responsibilities:
- HFT execution
- shadow execution
- slippage modeling
- microstructure analysis
- tick processing
- risk throttling

---

## Replay + Audit Region

Detected:
- replay/
- DecisionAuditTrail
- trade_state_machine.py
- replay_store.py
- replay_validator.py

Responsibilities:
- replay continuity
- audit persistence
- execution reconstruction
- decision lineage

---

## Observability Region

Detected:
- observability/
- production_monitor.py
- performance_monitor.py
- failure_tracker.py
- logging_utils.py

Responsibilities:
- runtime visibility
- health monitoring
- failure tracking
- execution monitoring
- runtime diagnostics

---

## Broker + Exchange Region

Detected:
- broker_adapter.py
- dhan_client.py
- fyers_client.py
- exchange integrations
- websocket integrations

Responsibilities:
- broker abstraction
- order routing
- market connectivity
- execution transport
- portfolio synchronization

---

## Commodity Runtime Region

Detected:
- commodities/

Responsibilities:
- commodity ingestion
- feature engineering
- commodity signal generation
- exchange-linked execution preparation

---

## Finance Intelligence Region

Detected:
- financeKnowledge/
- finance_reasoning/

Responsibilities:
- reasoning workflows
- rule evaluation
- audit-aware reasoning
- knowledge ingestion
- financial intelligence processing

---

## Database + Persistence Region

Detected:
- db/
- migrations/
- mongo_client.py
- database.py
- samruddhi_memory.py

Responsibilities:
- runtime persistence
- portfolio persistence
- replay persistence
- memory systems
- migration management

---

# Deployment Topology Regions

Detected:
- deployment/
- Dockerfile
- docker-compose.yml
- render.yaml
- render_start.sh

Responsibilities:
- runtime startup
- deployment orchestration
- containerized execution
- Render deployment flow

---

# Runtime Ownership Findings

## Positive Signals

- strong modular runtime separation exists
- broker abstraction direction exists
- replay-aware architecture exists
- deployment preparation exists
- observability infrastructure exists

---

## Major Structural Risks

### Runtime Fragmentation
Multiple independently runnable runtime surfaces exist.

### Orchestration Duplication
mcp_service and mcp_server overlap operational responsibilities.

### Distributed Execution Ownership
Execution authority spans multiple runtime regions.

### Mixed Runtime Maturity
Stock runtime more operationally mature than crypto and commodity regions.

### Legacy/Experimental Surface Noise
Production runtime tree contains experimental, fallback, compatibility, and duplicate runtime regions.

---

# Conclusion

Phase 1 repository topology acquisition successfully mapped the operational architecture surface of Samruddhi.

The platform demonstrates:
- significant convergence maturity
- strong modular runtime layering
- replay-aware architecture
- broker abstraction evolution
- deployment preparation

However:
- runtime authority remains partially distributed
- orchestration convergence remains incomplete
- replay and observability convergence remain partially fragmented

Further canonicalization work is required to achieve one fully understandable and singular runtime organism.