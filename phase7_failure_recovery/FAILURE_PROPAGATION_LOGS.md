# FAILURE_PROPAGATION_LOGS.md

# Failure Propagation Evidence

---

# 1. INVALID BROKER RESPONSE

Source:
live_executor.py

Observed:

❌ DHAN ORDER REJECTED: Input_Exception (DH-905)

Behavior:
- explicit broker rejection logging
- failure propagated upward
- execution halted safely

---

# 2. INVALID SIGNAL REJECTION

Source:
test_signal_filter.py

Observed:
- Low confidence signal rejected
- Conflicting signal rejected
- High-risk signal rejected

Behavior:
- deterministic rejection
- no silent signal acceptance

---

# 3. TIMEOUT PROPAGATION

Source:
api_server.py

Observed:

HFT2 backend timeout

Behavior:
- timeout escalated through HTTPException
- no hidden timeout suppression

---

# 4. STALE DATA GOVERNANCE

Source:
live_price_validator.py

Observed:

Data is too stale for trading

Behavior:
- stale data warning surfaced
- stale execution prevention active

---

# 5. RETRY OBSERVABILITY

Source:
fyers_data_service.py

Observed:

Error in data update loop (attempt X)

Behavior:
- retries visible
- exponential backoff active
- retry count observable

---

# 6. CACHE INVALIDATION

Source:
dhan_client.py

Observed:

Cleared stale cache

Behavior:
- stale state actively invalidated
- cache lifecycle observable

---

# 7. VALIDATION FAILURE PROPAGATION

Source:
api_server.py

Observed:
- Invalid horizon
- Invalid symbol
- Invalid prediction
- Invalid quantity

Behavior:
- validation failure escalated
- request rejected deterministically

---

# 8. RECOVERY GOVERNANCE

Source:
multi_source_data_provider.py

Observed:
- recovery_time
- circuit breaker recovery
- deterministic fallback routing

Behavior:
- controlled provider recovery
- failure isolation architecture present

---

# Conclusion

Failure propagation remains:
- visible
- structured
- deterministic
- observable

No major silent failure suppression identified in core execution paths.