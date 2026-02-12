@echo off
echo ====================================
echo Starting Hugo + Netlify Dev Server
echo ====================================
echo.

REM Check if node_modules exists
if not exist "node_modules" (
    echo Installing dependencies...
    call npm install
    echo.
)

echo Starting Netlify Dev...
echo.
echo Site will be available at: http://localhost:8888
echo Admin panel: http://localhost:8888/admin/
echo.
echo Press Ctrl+C to stop the server
echo.

netlify dev
