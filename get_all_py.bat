@echo off
setlocal enabledelayedexpansion

REM Output file
set OUTPUT=all_python.txt

REM Clear old file
if exist "%OUTPUT%" del "%OUTPUT%"

echo ========================================== >> "%OUTPUT%"
echo ALL PYTHON FILES >> "%OUTPUT%"
echo ========================================== >> "%OUTPUT%"

for /r %%F in (*.py) do (
    echo. >> "%OUTPUT%"
    echo ========================================== >> "%OUTPUT%"
    echo FILE: %%F >> "%OUTPUT%"
    echo ========================================== >> "%OUTPUT%"

    type "%%F" >> "%OUTPUT%"
    echo. >> "%OUTPUT%"
)

echo Done. Output saved to %OUTPUT%
pause