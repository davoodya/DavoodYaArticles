# Hugo + PHP Server
Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host " Hugo with PHP Support" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Build Hugo
Write-Host "[1/2] Building Hugo site..." -ForegroundColor Yellow
hugo

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error building Hugo site!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[✓] Hugo build complete" -ForegroundColor Green
Write-Host ""

# Step 2: Start PHP Server
Write-Host "[2/2] Starting PHP Server..." -ForegroundColor Yellow
Write-Host ""
Write-Host "Server: " -NoNewline -ForegroundColor Yellow
Write-Host "http://localhost:1313" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop" -ForegroundColor Gray
Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

Set-Location public
php -S localhost:1313

Set-Location ..
