# DB_OWNERSHIP_MAP.md

# Database Ownership Map

## Primary Persistence Authority

| Storage Layer | Ownership Type |
|---|---|
| SQLite trading.db | PRIMARY |
| SQLite samruddhi_memory.db | PRIMARY |
| JSON cache files | SECONDARY |
| Runtime memory state | TRANSIENT |
| Redis cache | PERFORMANCE CACHE |

---

# Primary DB Components

| Component | Responsibility |
|---|---|
| database.py | DB initialization |
| portfolio_manager.py | Portfolio persistence |
| live_executor.py | Trade recording |
| samruddhi_memory.py | Memory persistence |

---

# Runtime Truth Regions

| Runtime Region | File | Risk |
|---|---|---|
| pending_orders | live_executor.py | replay-sensitive |
| active_orders | execution_tool.py | transient |
| user_state | web_backend.py | duplicate truth risk |
| portfolio cache | dhan_client.py | stale state risk |

---

# Migration Boundaries

Migration system identified:
JSON → SQLite

Migration files:
- initialize_db.py
- migrate.py
- database.py

---

# DB Risk Assessment

Current system still contains:
- transient runtime execution state
- multiple cache authorities
- runtime orchestration state

Replay-safe convergence not yet fully complete.