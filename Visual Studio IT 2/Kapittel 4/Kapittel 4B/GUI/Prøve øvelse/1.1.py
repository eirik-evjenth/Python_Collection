@echo off
:loop
start "" "https://example.com"
timeout /t 5 >nul
goto loop