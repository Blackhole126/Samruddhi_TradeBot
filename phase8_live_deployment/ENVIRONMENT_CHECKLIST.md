# ENVIRONMENT_CHECKLIST.md

# Production Deployment Checklist

## Required Environment Variables

### Authentication

- JWT_SECRET_KEY
- JWT_ALGORITHM

---

### Broker Credentials

- DHAN_ACCESS_TOKEN
- DHAN_CLIENT_ID
- FYERS_ACCESS_TOKEN
- FYERS_APP_ID

---

### AI / ML APIs

- GROQ_API_KEY
- ALPHA_VANTAGE_API_KEY
- GNEWS_API_KEY
- FMPC_API_KEY
- MARKETAUX_API_KEY

---

# Deployment Validation Checklist

| Validation | Status |
|---|---|
| Docker installed | REQUIRED |
| Docker Compose installed | REQUIRED |
| Python version pinned | REQUIRED |
| Requirements installed | REQUIRED |
| .env configured | REQUIRED |
| Secrets isolated | REQUIRED |
| Health endpoints reachable | REQUIRED |
| Logs directory writable | REQUIRED |
| Data persistence mounted | REQUIRED |

---

# Security Checklist

| Security Control | Status |
|---|---|
| No hardcoded broker credentials | REQUIRED |
| No API keys committed to git | REQUIRED |
| .env excluded from git | VALIDATED |
| JWT secret overridden | REQUIRED |
| Default admin credentials removed | REQUIRED |

---

# Runtime Verification

Validate:

- /tools/health returns healthy
- HFT2 backend reachable
- logs generated successfully
- Docker containers remain stable
- no crash loops observed
- observability logs visible

---

# Operational Recommendations

Recommended before live trading:

- centralized logging
- Prometheus monitoring
- Grafana dashboards
- replay-safe persistence convergence
- broker reconciliation validation
- execution audit pipeline
- immutable event store

---

# Deployment Status

Current readiness:
- development deployment: READY
- VPS deployment: READY
- production trading deployment: PARTIALLY READY

Further hardening required before production capital exposure.