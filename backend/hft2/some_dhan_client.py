import os
import logging
import requests
from .dhan_utils import handle_dhan_api_response, InvalidAuthError

BASE = "https://api.dhan.co/v2"

def dhan_get(path, **kwargs):
    """
    GET with one automatic refresh attempt on DH-901. Raises InvalidAuthError if auth cannot be fixed.
    """
    for attempt in range(2):  # attempt 0 = normal, attempt 1 = after possible refresh
        headers = {"Authorization": f"Bearer {os.getenv('DHAN_ACCESS_TOKEN')}"}                                                                                                                                            
        