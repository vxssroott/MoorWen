# ============================================================
# MOORWEN — AI DECISION ENGINE
# ============================================================

import random

def decide(env):
    # Simple AI decision engine — expandable
    if "bank" in env or "finance" in env:
        return "banking_payload"
    elif "crypto" in env or "exchange" in env:
        return "crypto_payload"
    elif "hospital" in env or "health" in env:
        return "hospital_payload"
    else:
        return "general_payload"

def deploy(decision):
    if decision == "banking_payload":
        import banking_payload
        banking_payload.run()
    elif decision == "crypto_payload":
        import crypto_payload
        crypto_payload.run()
    elif decision == "hospital_payload":
        import hospital_payload
        hospital_payload.run()
    else:
        import general_payload
        general_payload.run()

if __name__ == "__main__":
    env = input("Enter environment: ")
    decision = decide(env)
    deploy(decision)
