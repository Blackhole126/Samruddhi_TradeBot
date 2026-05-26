# EXTERNAL_ACKNOWLEDGEMENT_STRUCTURE.md

# External Acknowledgement Structure

## Objective

Document external broker acknowledgement lifecycle and execution mapping.

---

# 1. BROKER RESPONSE STRUCTURE

Observed broker response:

```python
order_response = self.dhan_client.place_order(...)
```

Expected response structure:

```json
{
  "status": "success",
  "orderId": "123456789",
  "message": "Order placed"
}
```

Failure structure:

```json
{
  "status": "failure",
  "errorType": "ValidationError",
  "errorCode": "DH-905",
  "errorMessage": "Rejected by broker"
}
```

---

# 2. ACKNOWLEDGEMENT EXTRACTION

Observed extraction logic:

```python
order_id = order_response.get("orderId") or order_response.get("order_id")
```

Purpose:
- normalize broker acknowledgement identifiers
- support multiple broker response formats

---

# 3. ACKNOWLEDGEMENT REGISTRATION

Observed runtime registration:

```python
self.pending_orders[order_id] = {
```

Purpose:
- maintain broker reconciliation continuity
- support lifecycle tracking
- support execution verification

---

# 4. EXECUTION RECONCILIATION

Observed reconciliation logic:

```python
for order_id, pending_order in list(self.pending_orders.items()):
```

Broker reconciliation:

```python
(o for o in all_orders if o.get("orderId") == order_id)
```

Purpose:
- synchronize external broker state
- validate execution completion
- resolve lifecycle states

---

# 5. LIFECYCLE RESOLUTION STATES

Observed states:

| State | Meaning |
|---|---|
| PENDING | awaiting broker execution |
| FILLED | execution completed |
| PARTIALLY_FILLED | partial execution |
| CANCELLED | cancelled by broker |
| REJECTED | broker rejection |

---

# 6. FAILURE OBSERVABILITY

Observed rejection visibility:

```python
❌ DHAN ORDER REJECTED
```

Observed propagation:

```python
return {"success": False, "message": ...}
```

Purpose:
- preserve external failure transparency
- prevent silent execution failure

---

# 7. TRACE CONTINUITY

Observed identifiers:

| Identifier | Purpose |
|---|---|
| request_id | request lineage |
| order_id | broker execution lineage |
| execution_status | lifecycle continuity |

---

# 8. REPLAY READINESS

Replay-supportive components identified:
- order_id persistence
- execution timestamps
- broker reconciliation
- lifecycle state transitions

Remaining gaps:
- partial in-memory state dependency
- immutable event persistence incomplete

---

# 9. CONCLUSION

External acknowledgement architecture demonstrates:
- structured broker acknowledgement handling
- observable execution lifecycle
- replay-supportive lifecycle continuity
- broker rejection transparency

System is structurally prepared for:
- broker execution validation
- external execution reconstruction
- lifecycle observability
- execution reconciliation workflows.