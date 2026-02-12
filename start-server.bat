@echo off
cls
echo.
echo ============================================
echo  Starting Development Servers
echo ============================================
echo.
echo Hugo Server: http://localhost:1313
echo PHP API:     http://localhost:8080
echo Admin Panel: http://localhost:8080/api/admin.php
echo.
echo Press Ctrl+C to stop both servers
echo.
echo ============================================
echo.

REM Start PHP built-in server in new window
start "PHP Server (Port 8080)" cmd /k "php -S localhost:8080 -t ."

REM Wait for PHP server to start
timeout /t 2 /nobreak >nul

REM Start Hugo server in current window
echo Starting Hugo Server...
hugo server -D

REM If Hugo stops, this will run
echo.
echo Hugo server stopped.
echo Please close the PHP server window manually.
pause
