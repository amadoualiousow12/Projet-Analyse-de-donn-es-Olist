<<<<<<< HEAD
# Projet d'Analyse de Données Olist

Ce projet est une version structurée et modulaire de votre analyse de données Olist, prête à être utilisée dans **VS Code**.

## 📂 Structure du Projet

- `data/` : Dossier destiné à recevoir vos fichiers CSV Olist.
- `src/` : Contient les modules Python :
  - `data_loader.py` : Chargement des fichiers CSV.
  - `cleanning.py` : Nettoyage et prétraitement des données.
  - `calculate_kpis.py` : Logique de calcul des indicateurs (CA, RFM, etc.).
  - `affichage_kpis.py` : Affichage textuel des résultats.
  - `viz.py` : Génération des graphiques.
  - `client.py` : Point d'entrée pour exécuter tout le pipeline.
- `notebook_original.ipynb` : Votre notebook d'origine pour référence.
- `requirements.txt` : Liste des dépendances nécessaires.
- `venv311/` & `venv313/` : Environnements virtuels pré-configurés.

## 🚀 Instructions d'Installation et d'Exécution

### 1. Préparation des données
Placez tous vos fichiers CSV Olist (ex: `olist_customers_dataset.csv`, etc.) dans le dossier `data/`.

### 2. Configuration de l'environnement dans VS Code
1. Ouvrez le dossier `olist_project` dans VS Code.
2. Ouvrez un terminal dans VS Code (`Ctrl+Shift+ù` ou `Terminal > New Terminal`).
3. Activez l'environnement de votre choix :
   - **Pour Python 3.11 :**
     ```bash
     source venv311/bin/activate  # Sur Linux/macOS
     # ou
     .\venv311\Scripts\activate   # Sur Windows
     ```
   - **Pour Python 3.13 :**
     ```bash
     source venv313/bin/activate
     ```
4. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

### 3. Exécution du projet
Pour lancer l'analyse complète, exécutez le script `client.py` :
```bash
python src/client.py
```

## 🛠️ Utilisation dans VS Code
- **Interpréteur Python** : Appuyez sur `Ctrl+Shift+P`, tapez "Python: Select Interpreter" et choisissez celui de `venv311` ou `venv313`.
- **Notebook** : Vous pouvez également ouvrir `notebook_original.ipynb` et choisir l'un des environnements comme noyau (kernel).
=======
# Projet-Analyse-de-donn-es-Olist
Ce projet consiste en une analyse exploratoire et statistique complète des données de Olist, la plus grande plateforme de vente en ligne au Brésil. À travers l'étude de plus de 100 000 commandes, l'objectif est d'extraire des indicateurs de performance (KPIs) et de comprendre le comportement des consommateurs.
>>>>>>> 7374fe569ac036374c55001bd425483d86abed5c
