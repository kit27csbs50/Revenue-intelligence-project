@echo off
echo.
echo ========================================
echo   Opening RevenueIQ Application
echo ========================================
echo.
echo Starting your default browser...
echo.
echo URL: http://127.0.0.1:5000
echo.

REM Wait a moment for server to be ready
timeout /t 2 /nobreak >nul

REM Open URL in default browser
start http://127.0.0.1:5000

echo.
echo Browser opened!
echo.
echo If you see a directory listing:
echo 1. Press Ctrl+Shift+Delete to clear cache
echo 2. Press Ctrl+Shift+N for incognito mode
echo 3. Navigate to http://127.0.0.1:5000 again
echo.
echo ========================================
echo.
pause
