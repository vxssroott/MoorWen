# ============================================================
# MOORWEN — VOIDWATCH
# ============================================================

import requests
import random
import time

def monitor_market():
    markets = [
        "https://api.binance.com/api/v3/ticker/price",
        "https://api.coinbase.com/v2/prices/spot"
    ]
    for market in markets:
        try:
            response = requests.get(market)
            if response.status_code == 200:
                data = response.json()
                print(f"[+] Market data: {data}")
                return data
        except:
            pass
    return None

def execute_micro_transaction(market_data):
    price = float(market_data.get("price", 0))
    amount = random.uniform(0.01, 0.1)
    print(f"[*] Executing micro‑transaction: {amount} at {price}")
    # Simulated transaction
    time.sleep(1)
    print("[+] Transaction complete.")

market_data = monitor_market()
if market_data:
    execute_micro_transaction(market_data)
