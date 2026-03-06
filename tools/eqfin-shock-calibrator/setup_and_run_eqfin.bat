@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
set "VENV_PY=%SCRIPT_DIR%.venv\Scripts\python.exe"

if exist "%VENV_PY%" goto RUN

echo [EQFIN] Creating local virtual environment...
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 -m venv "%SCRIPT_DIR%.venv"
) else (
  python -m venv "%SCRIPT_DIR%.venv"
)

if not exist "%VENV_PY%" (
  echo [EQFIN] Failed to create virtual environment.
  exit /b 1
)

:RUN
echo [EQFIN] Launching GUI...
"%VENV_PY%" "%SCRIPT_DIR%launch_eqfin_gui.py" %*
