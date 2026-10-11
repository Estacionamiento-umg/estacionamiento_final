@echo off
g++ motor_tarifas.cpp -o motor_tarifas.exe
if %errorlevel% neq 0 (
    echo No se pudo compilar. Verifica que g++ este instalado.
    pause
    exit /b
)
echo Compilacion correcta.
motor_tarifas.exe carro 121
echo.
pause
