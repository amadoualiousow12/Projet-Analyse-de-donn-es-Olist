def display_kpis(kpis):
    """Affiche les KPIs sous forme de tableaux et résumés."""
    print("\n" + "="*40)
    print("📊 RÉSUMÉ DES INDICATEURS CLÉS (KPIs)")
    print("="*40)

    print("\n--- Top 5 des mois avec le plus gros CA ---")
    print(kpis['ca_monthly'].sort_values('ca', ascending=False).head(5)[['year_month_str', 'ca', 'variation_pct']])

    print("\n--- Top 5 des produits les plus rentables ---")
    print(kpis['top_products'].head(5))

    print("\n--- Top 5 des catégories les plus vendues ---")
    print(kpis['top_5_categories'])

    print("\n--- Statistiques RFM Moyennes ---")
    print(kpis['rfm'][['recency', 'frequency', 'monetary']].mean().to_frame('Moyenne'))
    print("="*40 + "\n")
