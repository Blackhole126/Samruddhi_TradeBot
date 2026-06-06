# COMPATIBILITY_MATRIX.md

# Compatibility Matrix

## Objective

Document compatibility governance across major platform contracts.

---

# 1. CONTRACT COMPATIBILITY MATRIX

| Contract | Typed | Versioned | Lineage | Compatible | Risk |
|---|---|---|---|---|---|
| PredictRequest | YES | NO | YES | PARTIAL | MEDIUM |
| PredictionRequest | YES | NO | YES | PARTIAL | MEDIUM |
| AnalyzeRequest | YES | NO | YES | PARTIAL | MEDIUM |
| OrderRequest | YES | NO | PARTIAL | PARTIAL | HIGH |
| PlaceOrderRequest | YES | NO | PARTIAL | PARTIAL | HIGH |
| PortfolioMetrics | YES | NO | PARTIAL | PARTIAL | MEDIUM |
| Broker Responses | PARTIAL | NO | PARTIAL | PARTIAL | HIGH |
| Replay Events | PARTIAL | NO | YES | PARTIAL | MEDIUM |

---

# 2. VERSION COMPATIBILITY STATUS

Observed:
- API versions exist
- model versions exist
- MCP versions exist

Missing:
- schema_version
- compatibility_version
- migration policy

Impact:
- schema drift risk
- replay instability
- ambiguous backward compatibility

---

# 3. EXECUTION COMPATIBILITY RISKS

Observed:
- multiple OrderRequest definitions
- mixed broker acknowledgement formats
- overlapping execution APIs

Impact:
- execution contract drift
- replay reconstruction inconsistency
- broker mapping ambiguity

---

# 4. PORTFOLIO COMPATIBILITY RISKS

Observed:
- dict-based portfolio payloads
- multiple portfolio structures
- dynamic schema evolution

Impact:
- portfolio replay instability
- schema drift risk
- inconsistent portfolio lineage

---

# 5. BROKER COMPATIBILITY RISKS

Observed:
- orderId vs order_id
- mixed broker response normalization
- inconsistent acknowledgement structures

Impact:
- execution replay ambiguity
- broker lifecycle reconstruction gaps

---

# 6. TRACE COMPATIBILITY STATUS

Observed:
- request_id continuity
- integration audit lineage
- lifecycle logging

Strong replay lineage compatibility foundations exist.

---

# 7. DETERMINISTIC CONTRACT STATUS

| Area | Status |
|---|---|
| typed contracts | Strong |
| validation | Strong |
| lineage | Strong |
| version governance | Weak |
| compatibility governance | Partial |
| replay-safe schemas | Partial |

---

# 8. FINAL COMPATIBILITY ASSESSMENT

The platform demonstrates:
- mature typed API contracts
- strong validation systems
- strong request lineage continuity

However:
- unified schema governance absent
- compatibility enforcement fragmented
- overlapping contract ownership exists
- deterministic schema locking incomplete

Further convergence required for:
- schema_version governance
- immutable compatibility policy
- deterministic schema evolution rules
- replay-safe contract migration guarantees