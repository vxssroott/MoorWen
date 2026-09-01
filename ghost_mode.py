# ============================================================
# MOORWEN — GHOST MODE
# ============================================================

import time

def run():
    print("[*] Entering ghost mode — sleeping...")
    while True:
        time.sleep(3600)  # Sleep for 1 hour
        print("[*] Waking up... checking for activity.")
        # Check for activity — if none, go back to sleep
        # In production, you'd check CPU, network, etc.

if __name__ == "__main__":
    run()
