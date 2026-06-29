"""
One-time fix: correct demat_client_id in MongoDB where a username was stored instead
of the numeric Dhan client ID. Extracts the real client ID from the JWT token payload.
Run once: python fix_demat_client_id.py
"""
import base64
import json
import sys
import os

# Load env
try:
    from pathlib import Path
    from dotenv import load_dotenv
    for _p in [Path(__file__).parent, Path(__file__).parent.parent]:
        for _f in ["env", ".env"]:
            if (_p / _f).exists():
                load_dotenv(_p / _f)
                break
except Exception:
    pass

sys.path.insert(0, os.path.dirname(__file__))


def _extract_client_id_from_jwt(token: str):
    try:
        parts = token.split(".")
        if len(parts) < 2:
            return None
        payload = parts[1] + "=" * (-len(parts[1]) % 4)
        data = json.loads(base64.urlsafe_b64decode(payload.encode("ascii")).decode("utf-8"))
        cid = data.get("dhanClientId") or data.get("dhan_client_id")
        return str(cid).strip() if cid else None
    except Exception:
        return None


def fix():
    from db.mongo_client import get_mongo_db
    db = get_mongo_db("trading")
    col = db["users"]

    users = list(col.find({"demat_access_token": {"$exists": True, "$ne": ""}}))
    print(f"Found {len(users)} users with demat credentials")

    fixed = 0
    for u in users:
        cid = (u.get("demat_client_id") or "").strip()
        token = (u.get("demat_access_token") or "").strip()

        # Only fix if client_id is non-numeric (i.e. a username was stored)
        if cid and not cid.isdigit() and token.startswith("eyJ"):
            real_cid = _extract_client_id_from_jwt(token)
            if real_cid:
                col.update_one(
                    {"_id": u["_id"]},
                    {"$set": {"demat_client_id": real_cid}}
                )
                print(f"  Fixed user '{u.get('username')}': '{cid}' -> '{real_cid}'")
                fixed += 1
            else:
                print(f"  WARNING: Could not extract client_id from JWT for user '{u.get('username')}'")
        else:
            print(f"  OK: user '{u.get('username')}' has client_id='{cid}'")

    print(f"\nDone. Fixed {fixed} user(s).")


if __name__ == "__main__":
    fix()
