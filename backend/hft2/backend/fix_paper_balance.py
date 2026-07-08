#!/usr/bin/env python3
"""
One-off script: set the PAPER portfolio's cash and starting_balance to 100000.
Run this from your backend directory, with the venv active:

    python fix_paper_balance.py

If your setup uses per-user portfolios, pass the user_id as an argument:

    python fix_paper_balance.py <user_id>
"""

import sys
from datetime import datetime
from portfolio_manager import DualPortfolioManager
from db.database import Portfolio

NEW_BALANCE = 100000.0


def main():
    user_id = sys.argv[1] if len(sys.argv) > 1 else None

    pm = DualPortfolioManager(user_id=user_id)

    session = pm.db.Session()
    try:
        filter_kwargs = {"mode": "paper"}
        if user_id is not None:
            filter_kwargs["user_id"] = user_id

        portfolio = session.query(Portfolio).filter_by(**filter_kwargs).first()

        if not portfolio:
            print(f"No paper portfolio found (filter={filter_kwargs}). Nothing to update.")
            return

        old_cash = portfolio.cash
        old_start = portfolio.starting_balance

        portfolio.cash = NEW_BALANCE
        portfolio.starting_balance = NEW_BALANCE
        portfolio.last_updated = datetime.now()

        session.commit()

        print(f"Updated paper portfolio (id={portfolio.id}):")
        print(f"  cash:              {old_cash} -> {portfolio.cash}")
        print(f"  starting_balance:  {old_start} -> {portfolio.starting_balance}")

    except Exception as e:
        session.rollback()
        print(f"Failed to update paper portfolio: {e}")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    main()