# DEPENDENCY MAP

## Phase
Phase 1 — Full Repo Acquisition + System Surface Mapping

---

# Objective

Identify and map:

- runtime dependencies
- infrastructure dependencies
- broker dependencies
- database dependencies
- deployment dependencies
- observability dependencies
- replay dependencies
- environment assumptions

---

# Core Runtime Dependencies

## Backend Runtime

Detected:
- FastAPI
- Uvicorn
- Pydantic
- asyncio
- websocket integrations

Purpose:
Primary runtime API execution and asynchronous orchestration.

---

## Data + ML Runtime

Detected:
- pandas
- numpy
- scikit-learn
- tqdm

Purpose:
Prediction runtime, feature engineering, signal generation, and analytics.

---

## Broker + Exchange Dependencies

Detected:
- Dhan integrations
- Fyers integrations
- ccxt integrations
- websocket broker handling

Purpose:
Market connectivity, execution routing, broker synchronization, exchange interaction.

---

## Database + Persistence Dependencies

Detected:
- SQLite
- MongoDB
- Alembic migrations
- SQLAlchemy
- persistence stores

Purpose:
- replay persistence
- portfolio persistence
- runtime storage
- audit storage
- migration handling

---

## Observability Dependencies

Detected:
- logging
- production monitoring
- performance monitoring
- failure tracking
- rotating log handlers

Purpose:
- runtime visibility
- operational diagnostics
- failure continuity
- observability persistence

---

## Replay + Audit Dependencies

Detected:
- replay_store.py
- replay_validator.py
- DecisionAuditTrail
- trade_state_machine.py

Purpose:
- execution reconstruction
- replay continuity
- decision lineage
- audit persistence

---

# Environment Variable Dependencies

Detected Runtime Variables:

- FYERS_APP_ID
- FYERS_ACCESS_TOKEN
- DHAN_CLIENT_ID
- DHAN_ACCESS_TOKEN
- DATABASE_URL
- MONGODB_URI
- REDIS_URL
- JWT_SECRET_KEY
- GROQ_API_KEY

Purpose:
- broker authentication
- exchange connectivity
- persistence configuration
- runtime authorization
- inference/runtime intelligence

---

# Deployment Dependencies

Detected:
- Docker
- Render deployment configuration
- docker-compose.yml
- render_start.sh
- runtime.txt

Purpose:
- deployment orchestration
- runtime startup
- container execution
- environment provisioning

---

# Replay + Runtime Continuity Dependencies

Detected:
- persistence fallback logic
- replay validation systems
- trade state persistence
- audit trail persistence

Current State:
Replay continuity exists operationally but globally singular replay persistence authority remains partial.

---

# Runtime Safety Dependencies

Detected:
- throttling systems
- risk envelopes
- drawdown protection
- integrated risk management
- validation layers

Purpose:
- fail-closed runtime behavior
- execution safety
- risk enforcement
- runtime protection

---

# Dependency Mapping Findings

## Positive Signals

- broker abstraction direction exists
- deployment preparation exists
- replay-aware dependencies exist
- observability dependencies operationally integrated
- multi-market runtime dependencies identified

---

## Major Dependency Risks

### Hidden Environment Assumptions
Runtime startup still heavily depends on undocumented environment setup.

---

### Credential Dependency Complexity
Broker connectivity depends on token lifecycle and exchange-specific authentication handling.

---

### Distributed Runtime Dependencies
Execution, replay, observability, and orchestration dependencies remain partially distributed.

---

### Deployment Dependency Fragmentation
Deployment assumptions currently span:
- Docker
- Render
- local runtime expectations
- environment-variable-driven startup

---

### Onboarding Dependency Risk
Fresh-machine startup validation exposed:
- hidden package assumptions
- incomplete dependency initialization
- onboarding friction regions

---

# Runtime Validation Findings

Fresh-device startup validation revealed:
- missing dependency assumptions
- hidden package requirements
- onboarding reconstruction gaps
- runtime initialization dependency chains

Detected runtime startup dependency chain included:
- yfinance
- FastAPI
- psutil
- tqdm
- scikit-learn
- python-jose

This operationally validated:
- dependency graph continuity
- runtime initialization order
- onboarding friction regions

---

# Conclusion

Dependency acquisition and mapping successfully identified the operational dependency structure of Samruddhi.

The platform demonstrates:
- strong multi-runtime dependency integration
- broker-aware runtime architecture
- replay-aware dependency layering
- deployment preparation maturity
- observability integration maturity

However:
- onboarding dependency reconstruction remains partially manual
- deployment dependency convergence remains incomplete
- hidden environment assumptions still exist
- runtime dependency ownership remains partially distributed

Further canonicalization and onboarding hardening are required to achieve deterministic environment reconstruction and deployment continuity.