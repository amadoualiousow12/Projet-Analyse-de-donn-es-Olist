import pandas as pd

def calculate_kpis(data):
    """Calcule les KPIs principaux (CA mensuel, Top produits, RFM)."""
    kpis = {}

    # Préparation du DataFrame principal (Orders + Items)
    df = data['orders'].merge(data['order_items'], on='order_id', how='inner')
    df = df[df['order_status'] == 'delivered']
    df['ca'] = df['price'] + df['freight_value']

    # 1. CA Mensuel
    df['year_month'] = df['order_purchase_timestamp'].dt.to_period('M')
    ca_monthly = df.groupby('year_month', as_index=False)['ca'].sum().sort_values('year_month')
    ca_monthly['ca_n_1'] = ca_monthly['ca'].shift(12)
    ca_monthly['variation_pct'] = ((ca_monthly['ca'] - ca_monthly['ca_n_1']) / ca_monthly['ca_n_1']) * 100
    ca_monthly['year_month_str'] = ca_monthly['year_month'].astype(str)
    kpis['ca_monthly'] = ca_monthly

    # 2. Top 10 Produits
    top_products = df.groupby('product_id', as_index=False).agg(ca=('ca', 'sum')).sort_values('ca', ascending=False).head(10)
    kpis['top_products'] = top_products

    # 3. Top 5 Catégories
    df_cat = df.merge(data['products'][['product_id', 'product_category_name']], on='product_id', how='left')
    df_cat = df_cat.merge(data['product_category'], on='product_category_name', how='left')
    top_5_categories = df_cat.groupby('product_category_name_english', as_index=False).agg(ca=('ca', 'sum')).sort_values('ca', ascending=False).head(5)
    kpis['top_5_categories'] = top_5_categories

    # 4. RFM
    df_rfm = df.merge(data['customers'][['customer_id', 'customer_unique_id']], on='customer_id', how='left')
    ref_date = df_rfm['order_purchase_timestamp'].max()
    rfm = df_rfm.groupby('customer_unique_id').agg(
        recency=('order_purchase_timestamp', lambda x: (ref_date - x.max()).days),
        frequency=('order_id', 'nunique'),
        monetary=('ca', 'sum')
    ).reset_index()

    # Scoring RFM
    for col, score_name in zip(['recency', 'frequency', 'monetary'], ['R_score', 'F_score', 'M_score']):
        try:
            rfm[score_name] = pd.qcut(rfm[col], q=5, labels=False, duplicates='drop') + 1
            if score_name == 'R_score':
                rfm[score_name] = 6 - rfm[score_name]
        except:
            rfm[score_name] = 1

    rfm['RFM_score'] = rfm['R_score'].astype(str) + rfm['F_score'].astype(str) + rfm['M_score'].astype(str)
    kpis['rfm'] = rfm

    # 5. Heatmap Data
    df['month'] = df['order_purchase_timestamp'].dt.month
    df['weekday'] = df['order_purchase_timestamp'].dt.day_name()
    heatmap_data = df.groupby(['weekday', 'month'])['ca'].sum().reset_index()
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    heatmap_pivot = heatmap_data.pivot(index='weekday', columns='month', values='ca').reindex(days_order)
    kpis['heatmap_pivot'] = heatmap_pivot

    print('Calcul des KPIs terminé.')
    return kpis
