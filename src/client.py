import os
import sys

# Ajouter le répertoire racine du projet au path pour les imports
# Cela permet d'importer depuis 'src' sans problème
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(ROOT_DIR, 'src'))

from data_loader import load_data
from cleanning import cleaning
from calculate_kpis import calculate_kpis
from affichage_kpis import display_kpis
from viz import visualize_data

def main():
    # Définition du chemin absolu vers le dossier data
    data_dir = os.path.join(ROOT_DIR, 'data')
    
    print(f"--- Démarrage du Pipeline Olist ---")
    print(f"Recherche des données dans : {data_dir}")
    
    # 1. Chargement
    data = load_data(data_dir)
    
    # Vérifier si les données essentielles sont chargées
    if data.get('orders') is None:
        print("\n❌ Erreur : Le fichier 'olist_orders_dataset.csv' est indispensable.")
        return

    # 2. Nettoyage
    data = cleaning(data)
    
    # 3. Calcul des KPIs
    kpis = calculate_kpis(data)
    
    # 4. Affichage des KPIs (Tableaux)
    display_kpis(kpis)
    
    # 5. Visualisation (Graphiques)
    print("Génération des graphiques...")
    visualize_data(kpis)
    
    print("--- Pipeline terminé avec succès ---")

if __name__ == "__main__":
    main()
