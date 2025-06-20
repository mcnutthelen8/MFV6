@echo off
setlocal enabledelayedexpansion

:loop
cd C:\Users\Administrator\Downloads\MFV6-main\MFV6-main

echo Killing Python and Chrome-related processes...
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im chrome.exe >nul 2>&1
taskkill /f /im chromedriver.exe >nul 2>&1
taskkill /f /im uc_driver.exe >nul 2>&1

echo Running Python script...
start "" cmd /c "python main_win10.py"

echo Waiting 30 minutes...
timeout /t 1800 /nobreak

echo Restarting script...
goto loop
