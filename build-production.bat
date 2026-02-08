@echo off
REM Build script for production deployment on Windows
REM Usage: build-production.bat

echo ==================================
echo Building Hugo Site for Production
echo ==================================
echo.
echo Base URL: https://davoodya.ir/articles/
echo.

REM Clean previous build
echo Cleaning previous build...
if exist public rmdir /s /q public

REM Build with production settings
echo Building site...
hugo --minify --cleanDestinationDir --gc --verbose

REM Check if build was successful
if %ERRORLEVEL% EQU 0 (
    echo.
    echo Build successful!
    echo.
    echo Output directory: public\
    echo.
    echo Ready to deploy!
    echo.
    echo Next steps:
    echo 1. Test the build locally
    echo 2. Upload 'public\' folder to: https://davoodya.ir/articles/
    echo.
) else (
    echo.
    echo Build failed!
    echo Please check the errors above.
    exit /b 1
)
