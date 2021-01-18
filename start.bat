@echo off

START cmd.exe /k "C:\Users\itf-infra\anaconda3\condabin\conda.bat activate & C:\Users\itf-infra\anaconda3\envs\house2\python.exe manage.py runserver 0.0.0.0:8000"
START cmd.exe /k "C:\Users\itf-infra\anaconda3\condabin\conda.bat activate & scrapyd.exe"
