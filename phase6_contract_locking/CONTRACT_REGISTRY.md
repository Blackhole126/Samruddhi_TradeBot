# CONTRACT_REGISTRY.md

# Contract Registry

## Objective

Lock major platform contracts for:
- deterministic execution
- replay safety
- schema governance
- compatibility validation
- lineage continuity

---

# 1. CONTRACT GOVERNANCE STATUS

Observed:
- extensive Pydantic schema usage
- structured request contracts
- typed validation systems
- API-level contract enforcement

Strong schema foundations already exist.

However:
- schema governance remains fragmented
- no unified schema_version governance exists
- compatibility ownership incomplete

---

# 2. PREDICTION CONTRACT

## Primary Contracts

Observed:

| Contract | Location |
|---|---|
| PredictRequest | api_server.py |
| PredictionRequest | web_backend.py |
| PredictRequest | api_wrapper.py |

---

## Core Fields

Observed fields include:
- symbol
- horizon
- risk_profile
- request_id
- metadata
- timestamp

---

## Lineage Fields

Observed:
- request_id
- timestamp
- metadata.request_id

---

## Validation

Observed:
- BaseModel validation
- Field validation
- typed request structures

---

## Governance Status

| Area | Status |
|---|---|
| schema typing | Strong |
| request lineage | Strong |
| schema versioning | Missing |
| compatibility governance | Partial |

---

# 3. EXECUTION CONTRACT

## Primary Contracts

Observed:

| Contract | Location |
|---|---|
| OrderRequest | hft/routes.py |
| OrderRequest | simple_app.py |
| PlaceOrderRequest | web_backend.py |

---

## Core Fields

Observed execution fields:
- symbol
- side
- quantity
- order_type
- product_type
- broker_response
- order_id

---

## Broker Lineage

Observed:
- order_response
- broker acknowledgement mapping
- order lifecycle tracking
- request_id logging

---

## Governance Status

| Area | Status |
|---|---|
| execution schemas | Strong |
| broker mapping | Strong |
| deterministic ordering | Partial |
| schema versioning | Missing |

---

# 4. PORTFOLIO CONTRACT

## Portfolio Structures Identified

Observed:
- PortfolioMetrics
- portfolio_data dict structures
- portfolio persistence records
- portfolio optimization payloads

---

## Core Fields

Observed:
- holdings
- total_value
- cash
- exposure
- risk_metrics
- allocations

---

## Governance Risks

Observed:
- multiple dynamic dict-based portfolio structures
- incomplete centralized schema ownership
- compatibility drift risk

---

# 5. BROKER ACKNOWLEDGEMENT CONTRACT

## Broker Structures Identified

Observed:
- order_response
- broker failure responses
- broker acknowledgement mapping

---

## Core Fields

Observed:
- orderId
- order_id
- errorCode
- errorType
- errorMessage
- status

---

## Governance Risks

Observed:
- mixed broker response formats
- partial normalization
- inconsistent acknowledgement structures

---

# 6. REPLAY EVENT CONTRACT

## Replay Structures Identified

Observed:
- integration_audit persistence
- request_id lineage
- execution event persistence
- JSONL replay artifacts

---

## Replay Fields

Observed:
- request_id
- timestamp
- endpoint
- symbol
- quantity
- event payloads

---

## Governance Status

| Area | Status |
|---|---|
| replay persistence | Strong |
| lineage continuity | Strong |
| immutable guarantees | Partial |
| schema governance | Partial |

---

# 7. VALIDATION SYSTEMS IDENTIFIED

Observed validation systems:

| Validation Type | Location |
|---|---|
| BaseModel typing | widespread |
| @validator | config_schema.py |
| Field validation | API contracts |
| typed request enforcement | multiple APIs |

---

# 8. VERSION GOVERNANCE STATUS

Observed:
- API versions
- MCP versions
- model versions
- KB versions

However:

```text
schema_version
```

was NOT found globally.

Critical finding:
- no unified schema_version governance exists.

Impact:
- compatibility drift risk
- replay reconstruction instability
- schema evolution ambiguity

---

# 9. OWNERSHIP GOVERNANCE

Observed ownership regions:

| Domain | Primary Owner |
|---|---|
| prediction contracts | api_server / mcp_adapter |
| execution contracts | live_executor / web_backend |
| broker contracts | dhan_client / live_executor |
| replay contracts | integration_audit |
| portfolio contracts | portfolio_manager |

---

# 10. CONTRACT LOCKING STATUS

Current state:

| Area | Status |
|---|---|
| typed schemas | Strong |
| request validation | Strong |
| lineage fields | Strong |
| compatibility governance | Partial |
| schema version governance | Weak |
| deterministic contracts | Partial |

---

# 11. CONCLUSION

The platform already demonstrates:
- mature schema foundations
- strong typed validation
- structured API governance
- request lineage continuity

However:
- unified schema_version governance absent
- compatibility enforcement fragmented
- multiple overlapping contract regions exist
- deterministic schema locking incomplete

Further convergence required for:
- immutable contract governance
- schema evolution policy
- replay-safe compatibility guarantees