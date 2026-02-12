# Development Server Starter
# This script runs both Hugo and PHP servers simultaneously

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host " Starting Development Servers" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Hugo Server: " -NoNewline -ForegroundColor Yellow
Write-Host "http://localhost:1313" -ForegroundColor Green
Write-Host "PHP API:     " -NoNewline -ForegroundColor Yellow
Write-Host "http://localhost:8080" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop both servers" -ForegroundColor Gray
Write-Host ""

# Start PHP built-in server in background
$phpJob = Start-Job -ScriptBlock {
    Set-Location $using:PWD
    php -S localhost:8080 -t .
}

Write-Host "[PHP Server] Starting on port 8080..." -ForegroundColor Magenta

# Wait a moment for PHP server to start
Start-Sleep -Seconds 2

# Start Hugo server (this will block)
Write-Host "[Hugo Server] Starting on port 1313..." -ForegroundColor Magenta
Write-Host ""

try {
    hugo server -D
}
finally {
    # Cleanup: Stop PHP server when Hugo stops
    Write-Host ""
    Write-Host "Stopping PHP server..." -ForegroundColor Yellow
    Stop-Job -Job $phpJob
    Remove-Job -Job $phpJob
    Write-Host "All servers stopped." -ForegroundColor Green
}
