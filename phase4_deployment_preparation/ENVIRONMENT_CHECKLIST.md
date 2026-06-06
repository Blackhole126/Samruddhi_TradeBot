# ENVIRONMENT CHECKLIST

## Phase
Phase 4 — Deployment Ownership Preparation

---

# Objective

Validate environment reconstruction readiness for:

- onboarding continuity
- deployment continuity
- runtime startup continuity
- VPS deployment preparation
- operational reproducibility

---

# Operating System Requirements

Validated Target Environments:

- Windows development environment
- Ubuntu VPS deployment environment

Recommended Production Environment:

```text
Ubuntu 22.04 LTS
```

---

# Required Runtime Software

## Python Runtime

Required:

```text
Python 3.12+
```

Validated Usage:
- backend runtime
- HFT runtime
- replay systems
- broker integrations
- observability systems

---

## Node.js Runtime

Required:

```text
Node.js + npm
```

Validated Usage:
- dashboard frontend
- frontend runtime
- deployment frontend continuity

---

## Git

Required:

```text
Git
```

Validated Usage:
- repo synchronization
- onboarding continuity
- deployment reconstruction

---

# Recommended Infrastructure Dependencies

## Redis

Recommended:

```text
Redis Server
```

Validated Usage:
- runtime caching
- async runtime coordination
- HFT runtime continuity

---

## PostgreSQL

Recommended:

```text
PostgreSQL
```

Current State:
- PostgreSQL convergence direction exists
- SQLite currently operationally active in multiple regions

---

## Docker

Recommended:

```text
Docker Desktop / Docker Engine
```

Validated Deployment Usage:
- Docker deployment topology
- containerized deployment continuity

---

# Python Environment Setup

## Create Virtual Environment

```powershell
python -m venv venv
```

---

## Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

---

# Backend Dependency Installation

Run:

```powershell
pip install -r requirements.txt
```

Additional runtime packages may be required depending on runtime surface reconstruction.

---

# Frontend Dependency Installation

Run:

```powershell
cd trading-dashboard
npm install
```

---

# Required Environment Variables

Validated Runtime Variables:

- JWT_SECRET
- DHAN_ACCESS_TOKEN
- DHAN_CLIENT_ID
- REDIS_URL
- DATABASE_URL

---

# Broker Runtime Requirements

Validated Broker Dependencies:

- Dhan credentials
- broker token continuity
- exchange connectivity
- websocket continuity

---

# Database Runtime Requirements

Validated Database Layers:

- SQLite
- Redis
- SQLAlchemy integration

Partially Validated:
- PostgreSQL deployment convergence

---

# Deployment Runtime Requirements

Validated Deployment Surfaces:

- Docker
- Render
- PM2 deployment regions
- NGINX deployment regions

---

# Runtime Startup Validation Checklist

Before startup validate:

- Python installed
- Node.js installed
- npm installed
- venv activated
- dependencies installed
- environment variables configured
- Redis available
- broker credentials configured

---

# Runtime Health Validation Checklist

After startup validate:

- backend API startup
- frontend startup
- HFT runtime startup
- broker initialization
- runtime logging visibility
- observability initialization
- database initialization

---

# Known Environment Risks

Detected Risks:

- missing Python dependencies
- dependency version conflicts
- invalid broker credentials
- Redis unavailable
- SQLite lock contention
- environment-variable absence
- websocket startup failures

---

# Environment Reconstruction Status

Current Status:

PARTIALLY VALIDATED

Validated:
- local runtime reconstruction
- backend startup continuity
- frontend startup continuity
- deployment surface continuity

Partially Validated:
- Ubuntu deployment continuity
- PostgreSQL convergence continuity
- PM2 orchestration continuity
- NGINX runtime continuity

Not Yet Fully Proven:
- production VPS reconstruction continuity
- globally canonical deployment environment continuity

---

# Conclusion

Samruddhi environment reconstruction readiness is operationally mature enough for onboarding preparation and deployment preparation validation.

However:
- production deployment continuity remains partial
- canonical deployment convergence remains incomplete
- environment standardization remains in-progress

Further deployment convergence work remains required before declaring fully hardened production deployment readiness.