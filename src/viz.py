import pandas as pd
import numpy as np

import matplotlib
matplotlib.use("Agg")  # backend sans interface graphique (AVANT pyplot)

import matplotlib.pyplot as plt
import seaborn as sns


def visualize_data(kpis):
    """Génère les visualisations à partir des KPIs."""
    sns.set(style="whitegrid")

    # 1. CA Mensuel
    plt.figure(figsize=(12, 6))
    ca_monthly = kpis['ca_monthly'].copy()
    ca_monthly['year_month_dt'] = pd.to_datetime(ca_monthly['year_month_str'])
    ca_monthly['ca_ma3'] = ca_monthly['ca'].rolling(window=3).mean()

    plt.plot(ca_monthly['year_month_dt'], ca_monthly['ca'], marker='o', label='CA mensuel')
    plt.plot(ca_monthly['year_month_dt'], ca_monthly['ca_ma3'],
             linestyle='--', label='Moyenne mobile 3 mois')

    plt.title('Chiffre d’affaires mensuel + Moyenne mobile 3 mois')
    plt.xlabel('Mois')
    plt.ylabel('CA (BRL)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("output/ca_mensuel.png")
    plt.close()

    # 2. Top 10 Produits
    plt.figure(figsize=(12, 6))
    top_products = kpis['top_products']

    plt.bar(top_products['product_id'], top_products['ca'])
    plt.title('Top 10 produits par chiffre d’affaires')
    plt.xlabel('Product ID')
    plt.ylabel('CA (BRL)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/top_products.png")
    plt.close()

    # 3. Heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(kpis['heatmap_pivot'], cmap='YlGnBu', annot=True, fmt='.0f')
    plt.title('Heatmap CA par jour de semaine et mois')
    plt.xlabel('Mois')
    plt.ylabel('Jour de semaine')
    plt.tight_layout()
    plt.savefig("output/heatmap_ca.png")
    plt.close()

    # 4. Distribution RFM
    plt.figure(figsize=(10, 6))
    plt.hist(np.log1p(kpis['rfm']['monetary']), bins=30)
    plt.title('Distribution de la valeur monétaire par client (log1p)')
    plt.xlabel('log(CA par client + 1)')
    plt.ylabel('Nombre de clients')
    plt.tight_layout()
    plt.savefig("output/rfm_distribution.png")
    plt.close()
