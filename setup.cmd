@echo off

@echo Extracting Embedded Python Interpreter
powershell.exe -NoP -NonI -Command "Expand-Archive .\bin.zip . -Force"
@echo.
@echo Extracting Windows Automation SDK (PowerShell) libraries
cd lib
powershell.exe -NoP -NonI -Command "Expand-Archive .\ext.zip . -Force"
cd ..

@echo.
@echo DONE.
