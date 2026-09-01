# ============================================================
# MOORWEN — SELF-DESTRUCT
# ============================================================

import os
import shutil

def run():
    print("[*] Self‑destruct initiated.")
    # Remove all MoorWen files
    shutil.rmtree("C:\\MoorWen", ignore_errors=True)
    # Remove registry entries
    os.system("reg delete HKCU\\Software\\MoorWen /f")
    os.system("reg delete HKLM\\Software\\MoorWen /f")
    # Remove service
    os.system("sc delete MoorWen")
    print("[+] MoorWen removed.")

if __name__ == "__main__":
    run()
