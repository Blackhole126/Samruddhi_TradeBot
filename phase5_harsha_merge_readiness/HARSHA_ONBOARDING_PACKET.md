# HARSHA ONBOARDING PACKET

## Phase
Phase 5 — Harsha Merge Readiness Layer

---

# Objective

Prepare Samruddhi onboarding continuity assuming the incoming builder has:

ZERO prior system knowledge.

This onboarding packet is intended to eliminate:
- tribal knowledge dependency
- hidden runtime assumptions
- undocumented startup behavior
- onboarding ambiguity
- deployment reconstruction confusion

Primary onboarding goal:

```text
first successful local run
without tribal knowledge
```

---

# 1. WHAT SAMRUDDHI IS

Samruddhi is a multi-market trading intelligence and execution platform designed around:

- stock runtime systems
- crypto runtime systems
- commodity runtime systems
- replay-aware execution
- observability-aware execution
- broker-linked execution
- portfolio continuity
- deployment-aware runtime behavior

The platform combines:

- prediction systems
- execution systems
- replay systems
- observability systems
- broker integrations
- HFT execution layers
- deployment orchestration

into one evolving canonical runtime organism.

---

# Core Runtime Objectives

Samruddhi aims to provide:

- replay-safe execution continuity
- observable runtime behavior
- broker-aware execution continuity
- deterministic execution direction
- deployment continuity
- onboarding-safe operational continuity

---

# Primary Runtime Regions

Validated runtime regions include:

- backend runtime
- HFT runtime
- MCP orchestration runtime
- broker runtime
- replay runtime
- observability runtime
- deployment runtime
- frontend runtime

---

# 2. SYSTEM ENTRY POINTS

## Primary Backend Entrypoint

Location:

```text
backend/api_server.py
```

Purpose:
- FastAPI startup
- runtime orchestration
- API exposure
- broker initialization
- observability startup

---

## HFT Runtime Entrypoints

Location:

```text
backend/hft2/backend/
```

Primary runtime regions:

```text
app.py
routes.py
live_executor.py
```

Purpose:
- HFT execution runtime
- live trading runtime
- broker execution continuity
- execution routing

---

## Frontend Entrypoint

Location:

```text
trading-dashboard/
```

Purpose:
- dashboard runtime
- frontend rendering
- runtime interaction layer

---

## Deployment Entrypoints

Validated deployment surfaces:

```text
docker-compose.yml
render.yaml
deployment/nginx
deployment/pm2
```

Purpose:
- deployment orchestration
- deployment continuity
- runtime startup continuity

---

# 3. HOW TO RUN

# Step 1 — Clone Repo

```powershell
git clone <repo-url>
```

---

# Step 2 — Create Virtual Environment

```powershell
python -m venv venv
```

---

# Step 3 — Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

---

# Step 4 — Install Backend Dependencies

```powershell
pip install -r requirements.txt
```

Additional runtime packages may also be required depending on runtime reconstruction.

---

# Step 5 — Install Frontend Dependencies

```powershell
cd trading-dashboard
npm install
```

---

# Step 6 — Start Backend Runtime

```powershell
cd backend
python api_server.py
```

Expected runtime initialization:
- FastAPI startup
- broker runtime initialization
- MCP runtime startup
- observability startup
- HFT proxy startup

---

# Step 7 — Start Frontend Runtime

```powershell
cd trading-dashboard
npm start
```

Expected runtime behavior:
- dashboard startup
- API connectivity
- runtime rendering continuity

---

# 4. CORE RUNTIME FLOW

Validated runtime lifecycle:

News/Input
→ Prediction
→ Signal
→ Execution
→ Portfolio
→ Replay
→ Observability

---

# Runtime Flow Breakdown

## Ingestion Runtime

Primary system:
- Samachar ingestion runtime

Responsibilities:
- news ingestion
- sentiment acquisition
- intelligence enrichment

---

## Prediction Runtime

Responsibilities:
- prediction generation
- signal enrichment
- prediction validation

---

## Execution Runtime

Responsibilities:
- execution orchestration
- broker-linked execution
- live execution continuity
- HFT execution continuity

---

## Portfolio Runtime

Responsibilities:
- portfolio synchronization
- execution truth persistence
- broker-linked portfolio continuity

---

## Replay Runtime

Responsibilities:
- replay continuity
- execution reconstruction
- audit persistence
- decision lineage continuity

---

## Observability Runtime

Responsibilities:
- runtime visibility
- failure visibility
- structured logging
- runtime diagnostics

---

# 5. COMMON FAILURE CASES

## Missing Python Dependencies

Symptoms:
- ModuleNotFoundError
- startup failures

Fix:
Install missing runtime packages.

---

## Broker Credential Failures

Symptoms:
- broker initialization failure
- authentication errors

Fix:
Validate:
- DHAN_ACCESS_TOKEN
- DHAN_CLIENT_ID
- broker token continuity

---

## Redis Runtime Failures

Symptoms:
- async runtime instability
- caching failures

Fix:
Ensure Redis runtime available.

---

## SQLite Lock Contention

Symptoms:
- persistence failures
- database lock errors

Fix:
Restart runtime and validate persistence continuity.

---

## Websocket Runtime Failures

Symptoms:
- exchange runtime interruption
- execution continuity gaps

Fix:
Validate network continuity and broker connectivity.

---

## Environment Variable Absence

Symptoms:
- startup failures
- runtime initialization failures

Fix:
Validate all required environment variables exist.

---

# 6. DEPLOYMENT NOTES

Validated deployment surfaces:

- Docker deployment
- Render deployment
- PM2 deployment regions
- NGINX deployment regions

---

# Current Deployment Status

Current Status:

PARTIALLY VALIDATED

Validated:
- Docker deployment continuity
- runtime startup continuity
- observability continuity
- deployment topology continuity

Partially Validated:
- PM2 orchestration continuity
- NGINX runtime continuity
- PostgreSQL convergence continuity

Not Yet Fully Proven:
- production VPS continuity
- replay-safe deployment restart continuity

---

# 7. DEBUGGING CHECKLIST

## Backend Debugging

Validate:
- backend startup logs
- import failures
- broker initialization logs
- runtime diagnostics
- async runtime errors

---

## Frontend Debugging

Validate:
- npm startup continuity
- API connectivity
- frontend rendering continuity

---

## Broker Debugging

Validate:
- broker credentials
- websocket continuity
- token freshness
- exchange connectivity

---

## Replay Debugging

Validate:
- replay persistence
- DecisionAuditTrail continuity
- replay validation continuity

---

## Observability Debugging

Validate:
- logger visibility
- runtime diagnostics
- failure tracking
- exception visibility

---

# 8. REPLAY / OBSERVABILITY NOTES

# Replay Notes

Validated replay regions:
- replay_store.py
- replay_validator.py
- DecisionAuditTrail
- trade_state_machine.py

Current replay state:
Replay-awareness operationally integrated but globally singular immutable replay authority remains partial.

---

# Observability Notes

Validated observability regions:
- structured logging
- production monitoring
- performance monitoring
- failure tracking

Current observability state:
Runtime visibility operationally integrated but globally unified telemetry continuity remains partial.

---

# 9. IMPORTANT FILES

## Critical Backend Files

```text
backend/api_server.py
backend/core/mcp_adapter.py
backend/hft2/backend/live_executor.py
backend/hft2/backend/routes.py
backend/runtime/canonical_runtime.py
```

---

## Replay + Audit Files

```text
replay_store.py
replay_validator.py
trade_state_machine.py
DecisionAuditTrail
```

---

## Deployment Files

```text
docker-compose.yml
render.yaml
deployment/nginx
deployment/pm2
backend/Dockerfile
```

---

## Observability Files

```text
production_monitor.py
performance_monitor.py
failure_tracker.py
```

---

# 10. SAFE TESTING WORKFLOW

# Recommended Safe Testing Order

## Step 1

Validate backend startup only.

---

## Step 2

Validate frontend startup only.

---

## Step 3

Validate API connectivity.

---

## Step 4

Validate observability continuity.

---

## Step 5

Validate replay continuity.

---

## Step 6

Validate broker runtime continuity in safe mode.

---

## Step 7

Validate execution flow using shadow execution before live execution.

---

# Important Safe Runtime Notes

DO NOT:
- directly test live execution without credential validation
- bypass replay validation
- bypass observability validation
- modify contracts silently
- introduce hidden runtime behavior

ALWAYS:
- validate runtime logs
- validate replay continuity
- validate broker initialization
- validate environment variables
- validate deployment continuity

---

# Current Platform Status

Current Operational State:

PARTIALLY CONVERGED

Strongly Validated:
- runtime continuity
- replay-awareness
- observability continuity
- broker abstraction direction
- deployment preparation
- onboarding preparation

Partially Validated:
- canonical replay convergence
- canonical observability convergence
- PM2 deployment continuity
- NGINX deployment continuity
- PostgreSQL convergence continuity

Not Yet Fully Proven:
- globally singular runtime authority
- replay-safe deployment restart continuity
- fully canonical deployment orchestration

---

# Final Notes For Incoming Builders

Samruddhi is a convergence-focused runtime platform.

The platform already demonstrates:
- strong runtime maturity progression
- replay-aware architecture
- observability-aware execution
- deployment preparation maturity
- onboarding preparation maturity

However:
- several runtime convergence regions remain in-progress
- replay authority remains partially fragmented
- observability authority remains partially distributed
- deployment convergence remains partially incomplete

Builders should prioritize:
- replay continuity
- observability continuity
- deterministic execution direction
- deployment continuity
- onboarding-safe operational behavior

while avoiding:
- isolated runtime forks
- hidden operational assumptions
- silent contract changes
- replay divergence
- deployment divergence