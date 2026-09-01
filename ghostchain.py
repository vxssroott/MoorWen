# ============================================================
# MOORWEN — GHOSTCHAIN
# ============================================================

import requests
import json

def scan_bridges():
    bridges = [
        "https://wormhole.com/bridge",
        "https://multichain.com/bridge",
        "https://axie.com/bridge"
    ]
    for bridge in bridges:
        try:
            response = requests.get(bridge)
            if response.status_code == 200:
                print(f"[+] Bridge found: {bridge}")
                return bridge
        except:
            pass
    return None

def drain_bridge(bridge_url):
    print(f"[*] Draining bridge: {bridge_url}")
    # Simulated drain logic
    payload = {"amount": 1000000, "destination": "attacker_wallet"}
    response = requests.post(f"{bridge_url}/drain", json=payload)
    if response.status_code == 200:
        print("[+] Bridge drained successfully.")
    else:
        print("[-] Drain failed.")

bridge = scan_bridges()
if bridge:
    drain_bridge(bridge)
