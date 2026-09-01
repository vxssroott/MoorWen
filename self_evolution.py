# ============================================================
# MOORWEN — SELF-EVOLUTION
# ============================================================

import os
import json

def analyze_environment():
    # Check OS, software, network, etc.
    env = {
        "os": os.name,
        "files": len(os.listdir(".")),
        "network": "connected" if os.system("ping -c 1 google.com") == 0 else "disconnected"
    }
    return env

def evolve(env):
    # Adjust behavior based on environment
    if env["network"] == "connected":
        print("[*] Network detected. Enabling propagation.")
        # Enable propagation module
        import network_propagation
        network_propagation.run()
    else:
        print("[*] No network. Staying silent.")
        # Enable ghost mode
        import ghost_mode
        ghost_mode.run()

if __name__ == "__main__":
    env = analyze_environment()
    evolve(env)
