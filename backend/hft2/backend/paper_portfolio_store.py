"""MongoDB-backed paper portfolio storage shared by execution and dashboard."""
from __future__ import annotations

import logging
from copy import deepcopy
from datetime import datetime
from typing import Any, Dict, List, Optional

PAPER_STARTING_BALANCE = 100000.0

logger = logging.getLogger(__name__)


def normalize_username(username: Optional[str]) -> str:
    return str(username or "anonymous").strip().lower() or "anonymous"


def default_paper_portfolio(starting_balance: float = PAPER_STARTING_BALANCE) -> Dict[str, Any]:
    balance = float(starting_balance or PAPER_STARTING_BALANCE)
    if balance <= 0:
        balance = PAPER_STARTING_BALANCE
    return {
        "cash": balance,
        "holdings": {},
        "starting_balance": balance,
        "realized_pnl": 0.0,
        "unrealized_pnl": 0.0,
        "trade_log": [],
    }


def _collection():
    from db.mongo_client import get_mongo_db

    db = get_mongo_db("trading")
    return db["paper_portfolios"]


def _clean_portfolio(data: Optional[Dict[str, Any]], starting_balance: float) -> Dict[str, Any]:
    cleaned = default_paper_portfolio(starting_balance)
    if not isinstance(data, dict):
        return cleaned

    for key in ("cash", "starting_balance", "realized_pnl", "unrealized_pnl"):
        if key in data:
            try:
                cleaned[key] = float(data.get(key) or 0)
            except (TypeError, ValueError):
                pass

    holdings = data.get("holdings")
    if isinstance(holdings, dict):
        cleaned["holdings"] = deepcopy(holdings)

    trade_log = data.get("trade_log")
    if isinstance(trade_log, list):
        cleaned["trade_log"] = deepcopy(trade_log)

    if cleaned["starting_balance"] <= 0:
        cleaned["starting_balance"] = PAPER_STARTING_BALANCE
    if not cleaned["holdings"] and not cleaned["trade_log"] and cleaned["cash"] <= 0:
        cleaned["cash"] = cleaned["starting_balance"]
    return cleaned


def load_paper_portfolio(
    username: Optional[str],
    starting_balance: float = PAPER_STARTING_BALANCE,
) -> Optional[Dict[str, Any]]:
    """Load a user's paper portfolio from MongoDB.

    Returns None when MongoDB is unavailable or no document exists so callers can
    fall back to legacy JSON files during local development.
    """
    un = normalize_username(username)
    if un == "anonymous":
        return None
    try:
        doc = _collection().find_one({"username": un, "mode": "paper"}, {"_id": 0})
        if not doc:
            return None
        portfolio = dict(doc.get("portfolio") or {})
        if "trade_log" not in portfolio and isinstance(doc.get("trade_log"), list):
            portfolio["trade_log"] = doc["trade_log"]
        return _clean_portfolio(portfolio, starting_balance)
    except Exception as exc:
        logger.warning("Could not load paper portfolio from MongoDB for %s: %s", un, exc)
        return None


def save_paper_portfolio(
    username: Optional[str],
    portfolio_data: Dict[str, Any],
    trade_log: Optional[List[Dict[str, Any]]] = None,
    starting_balance: float = PAPER_STARTING_BALANCE,
) -> bool:
    """Persist a user's paper portfolio to MongoDB."""
    un = normalize_username(username)
    if un == "anonymous":
        return False
    try:
        portfolio = _clean_portfolio(portfolio_data, starting_balance)
        if trade_log is not None:
            portfolio["trade_log"] = deepcopy(trade_log)
        _collection().update_one(
            {"username": un, "mode": "paper"},
            {
                "$set": {
                    "username": un,
                    "mode": "paper",
                    "portfolio": portfolio,
                    "trade_log": portfolio.get("trade_log", []),
                    "updated_at": datetime.utcnow(),
                },
                "$setOnInsert": {"created_at": datetime.utcnow()},
            },
            upsert=True,
        )
        return True
    except Exception as exc:
        logger.warning("Could not save paper portfolio to MongoDB for %s: %s", un, exc)
        return False


def load_paper_trade_log(username: Optional[str], limit: Optional[int] = None) -> Optional[List[Dict[str, Any]]]:
    portfolio = load_paper_portfolio(username)
    if portfolio is None:
        return None
    trades = portfolio.get("trade_log", [])
    if not isinstance(trades, list):
        trades = []
    return trades[-limit:] if limit else trades


def save_paper_trade_log(
    username: Optional[str],
    trade_log: List[Dict[str, Any]],
    portfolio_data: Optional[Dict[str, Any]] = None,
) -> bool:
    data = portfolio_data or default_paper_portfolio()
    return save_paper_portfolio(username, data, trade_log)
