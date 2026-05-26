# SAMRUDDHI STARTUP GUIDE

## Phase
Phase 4 — Deployment Ownership Preparation

---

# Objective

Provide a reproducible operational startup flow for:

- backend runtime
- frontend runtime
- HFT runtime
- deployment runtime
- observability startup
- broker runtime continuity

This guide is intended for:
- deployment preparation
- onboarding continuity
- runtime reconstruction
- operational startup validation
- Harsha onboarding readiness

---

# Platform Runtime Overview

Samruddhi currently contains:

- stock runtime systems
- crypto runtime systems
- commodity runtime systems
- HFT execution runtime
- replay runtime
- observability runtime
- deployment runtime
- broker runtime
- portfolio runtime

Primary runtime layers:

- FastAPI backend
- HFT execution backend
- MCP orchestration runtime
- broker integrations
- dashboard frontend
- deployment orchestration

---

# Repository Startup Structure

## Primary Runtime Regions

### Backend Runtime

Location:

```text
backend/
```

Primary entrypoint:

```text
backend/api_server.py
```

---

### HFT Runtime

Location:

```text
backend/hft2/backend/
```

Primary runtime regions:

```text
live_executor.py
app.py
routes.py
```

---

### Frontend Runtime

Location:

```text
trading-dashboard/
```

Primary runtime:

```text
npm frontend runtime
```

---

# Environment Preparation

## Required Software

Install:

- Python 3.12+
- Node.js
- npm
- Git

Recommended:
- Redis
- PostgreSQL
- Docker Desktop

---

# Virtual Environment Setup

## Create venv

Run:

```powershell
python -m venv venv
```

---

## Activate venv

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# Python Dependency Installation

## Install Backend Dependencies

Run from repo root:

```powershell
pip install -r requirements.txt
```

---

## Common Additional Runtime Packages

Some runtime regions may additionally require:

```powershell
pip install fastapi uvicorn psutil tqdm scikit-learn python-jose redis sqlalchemy python-dotenv websockets
```

---

# Frontend Dependency Installation

## Install Frontend Packages

Run:

```powershell
cd trading-dashboard
npm install
```

---

# Backend Startup

## Navigate to backend

```powershell
cd backend
```

---

## Start backend runtime

```powershell
python api_server.py
```

---

# Expected Backend Runtime Behavior

Expected runtime initialization:

- FastAPI startup
- MCP adapter initialization
- broker runtime initialization
- logging initialization
- HFT proxy initialization
- observability initialization
- async runtime initialization

---

# Frontend Startup

## Navigate to frontend

```powershell
cd trading-dashboard
```

---

## Start frontend runtime

```powershell
npm start
```

---

# HFT Runtime Expectations

Validated runtime regions:

- execution runtime
- live trading runtime
- portfolio runtime
- broker synchronization
- observability-linked runtime

---

# Deployment Runtime Surfaces

Validated deployment regions:

- Docker
- Render deployment
- PM2 deployment regions
- NGINX deployment regions
- runtime orchestration regions

Deployment files located:

```text
docker-compose.yml
render.yaml
backend/Dockerfile
deployment/nginx
deployment/pm2
```

---

# Runtime Health Validation

## Validate Backend Startup

Expected:
- API startup logs visible
- no import failures
- no missing dependency failures
- no broker initialization crashes

---

## Validate Runtime Logging

Expected:
- logger initialization
- startup logging
- runtime diagnostics
- async runtime visibility

---

## Validate Frontend Runtime

Expected:
- dashboard startup
- API connectivity
- runtime rendering continuity

---

# Required Environment Variables

Examples detected:

- JWT_SECRET
- DHAN_ACCESS_TOKEN
- DHAN_CLIENT_ID
- REDIS_URL
- DATABASE_URL

---

# Known Runtime Failure Regions

Detected startup failure regions:

- missing Python dependencies
- invalid broker credentials
- Redis unavailable
- SQLite lock contention
- environment variable absence
- dependency version conflicts
- websocket startup failures
- async runtime initialization failures

---

# Runtime Observability Expectations

Validated observability continuity:

- structured logging
- runtime diagnostics
- broker failure visibility
- async runtime visibility
- HFT runtime visibility
- execution-linked logging

---

# Startup Continuity Status

Current Status:

PARTIALLY VALIDATED

Validated:
- backend startup continuity
- frontend startup continuity
- runtime initialization continuity
- deployment runtime presence
- observability startup continuity

Partially Validated:
- PM2 orchestration continuity
- NGINX runtime continuity
- PostgreSQL convergence continuity
- deployment restart continuity

Not Yet Fully Proven:
- full production VPS deployment continuity
- globally canonical deployment orchestration
- deployment replay survivability

---

# Conclusion

Samruddhi startup reconstruction and deployment preparation are operationally mature enough for onboarding continuity and deployment preparation analysis.

However:
- production deployment convergence remains partial
- canonical deployment orchestration remains incomplete
- globally unified deployment continuity remains in-progress

Further deployment convergence work remains required before declaring fully hardened production runtime readiness.