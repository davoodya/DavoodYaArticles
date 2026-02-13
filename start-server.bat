@echo off
cls
echo.
echo ============================================
echo  Starting Hugo with PHP Server + Router
echo ============================================
echo.
echo [1/3] Building Hugo site...
hugo --cleanDestinationDir

echo.
echo [2/3] Checking router.php...
if exist "public\router.php" (
    echo ✓ Router script found
) else (
    echo ✗ Router script not found!
    echo   Please run: hugo --cleanDestinationDir
    pause
    exit /b 1
)

echo.
echo [3/3] Starting PHP Server with Router...
echo.
echo Server URL: http://localhost:1313
echo Custom 404: http://localhost:1313/test-404
echo.
echo Press Ctrl+C to stop the server
echo.
echo ============================================
echo.

REM Start PHP server with router script for custom 404
cd public
php -S localhost:1313 router.php

pause
