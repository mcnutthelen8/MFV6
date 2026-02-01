@echo off
TITLE MFV6 Bot Launcher

:: Change directory to your project folder
cd /d "C:\Users\Administrator\Downloads\MFV6-main\MFV6-main"

echo Starting MFV6 Scripts...

:: Start each script in a new window
::start "Browser Config" python browser_configure.py
::start "CSB Handle" python csb_handle.py
start "Main Bot" python main.py

