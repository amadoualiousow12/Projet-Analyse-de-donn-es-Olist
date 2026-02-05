@echo off
echo --- Configuration du projet Olist ---

echo Creation de l'environnement virtuel Python 3.11...
python -m venv venv311
echo Creation de l'environnement virtuel Python 3.13...
python -m venv venv313

echo Installation des dependances dans venv311...
call venv311\Scripts\activate
pip install -r requirements.txt
deactivate

echo Installation des dependances dans venv313...
call venv313\Scripts\activate
pip install -r requirements.txt
deactivate

echo --- Configuration terminee ! ---
pause
