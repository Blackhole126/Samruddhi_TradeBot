# ENTRY_POINTS_REPORT

## Objective

Identify and verify the runtime entry points of the Samruddhi TradeBot system.

This report documents:

* Where the system starts
* How the system boots
* What was executed
* What worked
* Primary API surface
* Remaining unknowns

Only evidence-backed observations are marked as verified.

---

# SYSTEM ENTRY POINTS

## Backend Entry Path

Primary backend entry point:

```text
backend/api_wrapper.py
```

Framework:

```text
FastAPI
```

Purpose:

* Expose stock analysis APIs
* Execute prediction workflows
* Serve health endpoints
* Act as primary backend runtime

---

## Frontend Entry Path

Frontend entry point:

```text
trading-dashboard/src/main.tsx
```

Frontend bootstrap path:

```text
index.html
    ↓
main.tsx
    ↓
React Dashboard
```

Framework:

```text
React + TypeScript + Vite
```

Purpose:

* Dashboard UI
* Analysis visualization
* Backend interaction

Verification status:

```text
Not verified during this review.
```

---

## Additional Runtime Entry Points

### MCP Trading Service

```text
backend/hft2/mcp_service/main.py
```

Purpose:

* Trading reasoning
* MCP protocol handling
* Agent orchestration

Evidence available:

```text
Runtime startup logs observed.
```

---

### Samachar News Service

```text
backend/samachar/api_server.py
```

Purpose:

* News ingestion
* News processing pipeline
* Contract validation

Verification status:

```text
Not verified during this review.
```

---

### Discipline Service

```text
backend/discipline_api.py
```

Purpose:

* Risk management
* Trade discipline enforcement

Verification status:

```text
Not verified during this review.
```

---

# WHERE THE SYSTEM STARTS

Observed startup candidates:

Backend:

```text
backend/api_wrapper.py
```

Frontend:

```text
trading-dashboard/src/main.tsx
```

Container orchestration:

```text
docker-compose.yml
```

Evidence source:

* Repository structure
* Entry point documentation
* Runtime screenshots

---

# HOW THE SYSTEM BOOTS

Observed backend boot sequence:

```text
api_wrapper.py
    ↓
FastAPI Application
    ↓
HTTP Endpoints
    ↓
Prediction Services
```

Observed HFT2 runtime boot sequence:

```text
run_hft2.py
    ↓
Data Service Initialization
    ↓
MCP Service Initialization
    ↓
Scheduler Initialization
    ↓
Trading Components Loaded
    ↓
Backend Ready
```

Evidence:

Runtime startup log screenshot.

Verified log entries include:

```text
Started web_backend (5000)

Live trading components loaded successfully

Market data cache database initialized

DataAgent initialized with scheduler

RL scanning agents loaded successfully

MCP Service components loaded successfully

Production core components loaded successfully

Configuration schema validation loaded successfully
```

---

# PRIMARY RUNTIME STARTUP COMMANDS

## Backend

```bash
cd backend
python api_wrapper.py
```

Alternative:

```bash
uvicorn api_wrapper:app --host 0.0.0.0 --port 8000
```

---

## Frontend

```bash
cd trading-dashboard
npm run dev
```

---

## HFT2 Runtime

```bash
python run_hft2.py
```

Observed from startup logs.

---

## Docker Runtime

```bash
docker-compose up -d
```

Verification status:

```text
Not independently verified during review.
```

---

# PRIMARY API SURFACE

## Health Endpoint

Endpoint:

```http
GET /tools/health
```

Observed request:

```http
GET http://localhost:8000/tools/health
```

Observed result:

```http
HTTP 200 OK
```

Observed response:

```json
{
  "status": "healthy",
  "models": {
    "available": true
  }
}
```

Status:

```text
VERIFIED
```

---

## Analysis Endpoint

Endpoint:

```http
POST /analyze
```

Purpose:

```text
Stock prediction and analysis.
```

Verification status:

```text
Endpoint identified.
Execution evidence not provided.
```

---

# WHAT WAS EXECUTED

Evidence provided shows execution of:

## Health Check

```http
GET /tools/health
```

Observed result:

```text
HTTP 200
Status: healthy
```

---

## HFT2 Runtime Startup

Observed startup log:

```text
Started web_backend (5000)

Live trading components loaded successfully

Market Data Client initialized

DataAgent initialized

Scheduler started

RL scanning agents loaded

MCP Service components loaded

Production core components loaded

Configuration schema validation loaded
```

---

# WHAT WORKED

Verified through supplied evidence.

## Backend API Startup

Status:

```text
VERIFIED
```

Evidence:

* Successful FastAPI response
* Uvicorn serving requests

---

## Health Endpoint

Status:

```text
VERIFIED
```

Evidence:

```text
GET /tools/health

HTTP 200

status = healthy
```

---

## HFT2 Backend Startup

Status:

```text
VERIFIED
```

Evidence:

```text
Started web_backend (5000)
```

---

## MCP Initialization

Status:

```text
VERIFIED
```

Evidence:

```text
MCP Service components loaded successfully
```

---

## Scheduler Initialization

Status:

```text
VERIFIED
```

Evidence:

```text
DataAgent initialized with scheduler
Market scan scheduled
```

---

## Configuration Validation

Status:

```text
VERIFIED
```

Evidence:

```text
Configuration schema validation loaded successfully
```

---

# EVIDENCE REVIEW

Evidence supplied:

* Backend health-check screenshot
* HTTP 200 response screenshot
* Runtime startup logs
* HFT2 backend startup logs
* MCP initialization logs
* Scheduler initialization logs
* Configuration validation logs

Evidence supports:

* Backend runtime startup
* Health endpoint operation
* MCP service initialization
* Scheduler initialization
* HFT2 backend startup

---

# REMAINING UNKNOWNS

The following items remain unverified:

1. Frontend startup execution.
2. POST /analyze endpoint execution.
3. End-to-end prediction workflow.
4. Samachar service startup.
5. Discipline API startup.
6. Docker Compose startup validation.
7. MongoDB runtime validation.
8. Redis runtime validation.
9. Broker integration validation.
10. Full production deployment sequence.

Unknown items are intentionally retained until supporting evidence is available.

---

# CONCLUSION

Observed Backend Entry Point:

```text
backend/api_wrapper.py
```

Observed Frontend Entry Point:

```text
trading-dashboard/src/main.tsx
```

Observed Primary API Surface:

```text
GET /tools/health
POST /analyze
```

Verified Runtime Components:

```text
✓ Backend API Startup
✓ Health Endpoint
✓ HFT2 Backend Startup
✓ MCP Initialization
✓ Scheduler Initialization
✓ Configuration Validation
```

Verification Status:

```text
PARTIALLY VERIFIED
```

Reason:

```text
Runtime evidence confirms backend startup and health functionality.
Several supporting services remain unverified and are retained as unknowns.
```
