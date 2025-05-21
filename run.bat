@echo off
echo Titanic Survival Prediction - Running Application
echo =============================================

echo.
echo Activating virtual environment...
call venv\Scripts\activate
if %ERRORLEVEL% neq 0 (
    echo Failed to activate virtual environment.
    echo Please run setup.bat first to set up the project.
    pause
    exit /b 1
)

echo.
echo Starting Flask web server...
echo.
echo Once the server is running, open your web browser and go to:
echo http://127.0.0.1:5000/
echo.
echo Press Ctrl+C to stop the server when you're done.
echo.
python app.py 