@echo off
echo Titanic Survival Prediction - Setup Script
echo ======================================

echo.
echo Step 1: Creating virtual environment...
python -m venv venv
if %ERRORLEVEL% neq 0 (
    echo Failed to create virtual environment.
    echo Please make sure Python is installed and added to PATH.
    pause
    exit /b 1
)

echo.
echo Step 2: Activating virtual environment...
call venv\Scripts\activate
if %ERRORLEVEL% neq 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b 1
)

echo.
echo Step 3: Installing required packages...
pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo Failed to install required packages.
    pause
    exit /b 1
)

echo.
echo Step 4: Training the machine learning model...
cd model
python train.py
if %ERRORLEVEL% neq 0 (
    echo Failed to train the model.
    cd ..
    pause
    exit /b 1
)
cd ..

echo.
echo Setup completed successfully!
echo.
echo To run the application:
echo 1. Run "run.bat"
echo 2. Open your web browser and go to: http://127.0.0.1:5000/
echo.
pause 