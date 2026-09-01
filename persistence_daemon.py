# ============================================================
# MOORWEN — PERSISTENCE DAEMON
# ============================================================

import os
import platform

def install_windows():
    print("[*] Installing as Windows Service")
    # Simulated Windows Service installation
    os.system("sc create MoorWen binPath= C:\\MoorWen\\moorwen.exe start= auto")

def install_linux():
    print("[*] Installing as Linux Daemon")
    # Simulated Linux Daemon installation
    os.system("systemctl enable moorwen.service")

def run():
    if platform.system() == "Windows":
        install_windows()
    elif platform.system() == "Linux":
        install_linux()
    else:
        print("[-] Unsupported OS")

if __name__ == "__main__":
    run()
