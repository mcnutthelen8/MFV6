@echo off
setlocal enabledelayedexpansion

:loop
cd C:\Users\Administrator\Downloads\MFV6-main\MFV6-main

echo Killing python and chrome processes...
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im chrome.exe >nul 2>&1

echo Checking internet connection...
ping -n 2 google.com >nul
if errorlevel 1 (
    echo Internet is down. Restarting Mysterium VPN...

    taskkill /f /im mysterium_vpn.exe >nul 2>&1
    timeout /t 5 >nul

    echo Starting Mysterium VPN...
    start "" "C:\Users\Administrator\Downloads\myst_win\myst_win\mysterium_vpn.exe"
) else (
    echo Internet is working fine.
)

echo Running Python script...
start "" cmd /c "python main_win10.py"

echo Waiting 1 hour...
timeout /t 1800 /nobreak

echo Restarting script...
goto loop
