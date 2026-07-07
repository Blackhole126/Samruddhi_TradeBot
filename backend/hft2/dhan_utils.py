import os
import threading
import logging
import requests
from dotenv import load_dotenv, set_key

ENV_PATH = os.path.join(os.path.dirname(__file__), "env")
load_dotenv(dotenv_path=ENV_PATH)

DHAN_CLIENT_ID = os.getenv("DHAN_CLIENT_ID")
DHAN_REFRESH_TOKEN = os.getenv("DHAN_REFRESH_TOKEN")  # set this in env if available

_refresh_lock = threading.Lock()

class InvalidAuthError(Exception):
    pass

def refresh_dhan_access_token(refresh_url: str = "https://api.dhan.co/v2/oauth/refresh"):
    """
    Refresh DHAN access token. Replace payload/endpoint if Dhan uses a different scheme.
    Requires DHAN_REFRESH_TOKEN to be set in env.
    """
    if not DHAN_REFRESH_TOKEN:
        raise InvalidAuthError("Missing DHAN_REFRESH_TOKEN in env")

    payload = {"client_id": DHAN_CLIENT_ID, "refresh_token": DHAN_REFRESH_TOKEN}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(refresh_url, json=payload, headers=headers, timeout=30)
    try:
        resp.raise_for_status()
    except Exception as e:
        logging.error("Failed to refresh DHAN token: %s %s", resp.status_code, resp.text)
        raise InvalidAuthError("Failed to refresh DHAN token") from e

    data = resp.json()
    new_token = data.get("access_token") or data.get("token") or data.get("accessToken")
    if not new_token:
        logging.error("DHAN refresh response missing token: %s", data)
        raise InvalidAuthError("Refresh response missing access token")

    # persist to env file
    set_key(ENV_PATH, "DHAN_ACCESS_TOKEN", new_token)
    os.environ["DHAN_ACCESS_TOKEN"] = new_token
    logging.info("DHAN access token refreshed and written to env")
    return new_token

def handle_dhan_api_response(response):
    """
    If response indicates DH-901, try to refresh token once and return the new token.
    Caller should retry the request if refreshed==True.
    """
    try:
        if response.status_code == 401:
            body = {}
            try:
                body = response.json()
            except Exception:
                pass
            if body.get("errorCode") == "DH-901" or body.get("errorType") == "Invalid_Authentication":
                logging.warning("DHAN invalid authentication detected (DH-901). Attempting refresh.")
                with _refresh_lock:
                    # double-check current token hasn't already been rotated by another thread/process
                    try:
                        new_token = refresh_dhan_access_token()
                        return {"refreshed": True, "access_token": new_token}
                    except InvalidAuthError as e:
                        logging.error("DHAN token refresh failed: %s", e)
                        return {"refreshed": False, "error": str(e)}
    except Exception as e:
        logging.exception("Error handling DHAN response: %s", e)
    return {"refreshed": False}