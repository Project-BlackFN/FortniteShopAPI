@echo off
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
  echo pip install failed.
  pause
  exit /b %errorlevel%
)
python -m shop_api.app