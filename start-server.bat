@echo off
cls
echo.
echo ============================================
echo  Starting Hugo with PHP Support
echo ============================================
echo.
echo [1/3] Building Hugo site...
hugo

echo.
echo [2/3] Starting PHP Server...
echo.
echo Server will run on: http://localhost:1313
echo.
echo Press Ctrl+C to stop
echo.
echo ============================================
echo.

REM Start PHP built-in server using public folder
cd public
php -S localhost:1313

pause
