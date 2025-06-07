

@echo off
:loop
cd C:\Users\WhatUpTime.com\Downloads\MFV6-main\MFV6-main
echo Killing python and chrome processes...
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im chrome.exe >nul 2>&1

echo Running Python script...
start "" cmd /c " python main5.py

echo Waiting 1 hour...
timeout /t 3600 /nobreak

echo Restarting script...
goto loop
