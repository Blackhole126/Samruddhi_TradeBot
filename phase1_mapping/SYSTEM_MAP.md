# SYSTEM_MAP.md

# Phase 1 — Full Repo Acquisition + System Mapping

## Objective

Map the complete Samruddhi + Trade_Bot architecture and identify:
- active services
- execution paths
- hidden runtime dependencies
- duplicate truth regions
- DB ownership boundaries
- mock/simulation paths
- replay-sensitive runtime state

---

# 1. SYSTEM OVERVIEW

The system is a multi-service trading intelligence and execution platform composed of:
- frontend dashboard
- orchestration APIs
- execution backend
- broker integration layers
- portfolio persistence
- observability systems
- runtime cache layers
- replay-sensitive execution state

Architecture follows:
Frontend → Backend Authority → Execution Layer → Broker Layer → Persistence

---

# 2. PRIMARY ENTRY POINTS

| File | Responsibility |
|---|---|
| backend/api_server.py | Primary orchestration + API layer |
| backend/hft/routes.py | HFT route aggregation |
| backend/hft2/backend/web_backend.py | Core execution backend |
| backend/hft2/backend/live_executor.py | Centralized execution engine |
| backend/hft2/backend/broker_adapter.py | Broker abstraction layer |
| backend/hft2/backend/dhan_client.py | Dhan broker integration |

---

# 3. ACTIVE SERVICES

| Service | Purpose |
|---|---|
| Trading Dashboard | Frontend visualization layer |
| API Server | API orchestration |
| Web Backend | Trading execution orchestration |
| LiveTradingExecutor | Centralized execution authority |
| Broker Adapter | Unified broker abstraction |
| Dhan Client | Live broker execution |
| Portfolio Manager | Portfolio persistence |
| MCP Execution Tool | Execution contract layer |
| Shadow Execution Simulator | Simulation/paper execution |
| Samachar Pipeline | News ingestion pipeline |
| Observability/Logging | Runtime monitoring |

---

# 4. EXECUTION ARCHITECTURE

Canonical execution flow identified:

Frontend
→ web_backend.py
→ live_executor.place_order()
→ dhan_client.place_order()
→ portfolio_manager.record_trade()
→ SQLite persistence

Execution consolidation appears partially completed successfully.

---

# 5. CONFIRMED ARCHITECTURAL FINDINGS

## Confirmed Centralized Execution
Most live execution routes correctly converge into:
- LiveTradingExecutor
- centralized broker access
- unified trade recording

## Confirmed Legacy Bypass
Legacy execution path identified:

simple_app.py
→ place_order_market()
→ dhan_client.py

This bypasses:
- LiveTradingExecutor
- centralized execution governance
- unified observability

Risk:
- duplicate execution authority
- replay inconsistency
- fragmented lifecycle tracking

---

# 6. RUNTIME STATE REGIONS

Replay-sensitive runtime state identified:

| Runtime State | File |
|---|---|
| pending_orders | live_executor.py |
| active_orders | execution_tool.py |
| user_state | web_backend.py |
| bot runtime state | web_backend.py |
| portfolio cache | dhan_client.py |

---

# 7. CACHE REGIONS

Multiple cache authorities identified:

| Cache Type | Location |
|---|---|
| JSON cache | stock_analysis_complete.py |
| Request cache | request_cache.py |
| Redis cache | app.py |
| Portfolio cache | dhan_client.py |
| Data service cache | data_service_client.py |
| Multi-source cache | multi_source_data_provider.py |

---

# 8. DATABASE BOUNDARIES

Primary DB authority:
- SQLite

Primary DB files:
- trading.db
- samruddhi_memory.db

DB ownership centralized under:
backend/hft2/backend/db/

Migration support exists:
JSON → SQLite

---

# 9. MOCK / SIMULATION PATHS

Mock/simulation systems identified:

| Component | Purpose |
|---|---|
| shadow_execution/simulator.py | Shadow execution |
| execution_router.py | Simulation routing |
| paper trading stubs | Legacy/testing support |

---

# 10. PHASE 1 STATUS

Completed:
- architecture mapping
- execution path tracing
- broker path validation
- runtime dependency identification
- DB ownership discovery
- replay-sensitive state discovery
- mock path identification