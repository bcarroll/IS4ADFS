@echo off
set IS4ADFS_PATH=%~dp0
cd %IS4ADFS_PATH%
set PATH=bin;bin\Scripts
bin\python.exe app.py %*