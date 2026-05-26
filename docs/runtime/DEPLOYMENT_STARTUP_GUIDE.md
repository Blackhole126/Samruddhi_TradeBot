# Deployment Startup Guide

## Objective

Define canonical runtime startup behavior for deployment convergence.

---

# Startup Sequence

Canonical startup flow:

1. environment initialization
2. replay layer initialization
3. observability layer initialization
4. canonical runtime initialization
5. API runtime startup
6. health check validation

---

# PM2 Startup

Example PM2 startup:

```bash
pm2 start deployment/pm2/ecosystem.config.js
```

---

# NGINX Startup

Example NGINX activation:

```bash
sudo systemctl restart nginx
```

---

# Health Validation

Deployment startup must validate:

- API availability
- replay persistence continuity
- observability persistence continuity
- runtime trace visibility

---

# Governance Guarantees

Deployment startup behavior remains:

- deterministic
- replay-safe
- observable
- trace-aware
- fail-visible