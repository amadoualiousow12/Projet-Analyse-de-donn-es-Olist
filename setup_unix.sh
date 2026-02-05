#!/bin/bash
echo "--- Configuration du projet Olist ---"

echo "Creation de l'environnement virtuel Python 3.11..."
python3 -m venv venv311
echo "Creation de l'environnement virtuel Python 3.13..."
python3 -m venv venv313

echo "Installation des dependances dans venv311..."
source venv311/bin/activate
pip install -r requirements.txt
deactivate

echo "Installation des dependances dans venv313..."
source venv313/bin/activate
pip install -r requirements.txt
deactivate

echo "--- Configuration terminee ! ---"
