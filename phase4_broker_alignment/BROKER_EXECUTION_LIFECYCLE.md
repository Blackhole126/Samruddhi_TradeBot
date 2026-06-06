# BROKER_EXECUTION_LIFECYCLE.md

# Broker Execution Lifecycle Diagram

```text
MARKET SIGNAL
    ↓
Prediction Engine
    ↓
Signal Contract Validation
    ↓
Execution Trigger
    ↓
live_executor.py
    ↓
broker_adapter.py
    ↓
dhan_client.place_order()
    ↓
BROKER API
    ↓
Broker Response Received
    ↓
order_response Validation
    ↓
order_id Extraction
    ↓
pending_orders Registration
    ↓
Execution Reconciliation Loop
    ↓
Broker Order Status Fetch
    ↓
Lifecycle Resolution

Possible States:
    → PENDING
    → FILLED
    → PARTIALLY_FILLED
    → REJECTED
    → CANCELLED

    ↓
executed_orders Persistence
    ↓
Portfolio Update
    ↓
Execution Logging
    ↓
Observability Layer
    ↓
Replay / Audit Reconstruction
```