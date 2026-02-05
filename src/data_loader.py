import pandas as pd
import os

def load_data(data_dir='data/'):
    """Charge les datasets Olist depuis le répertoire spécifié."""
    datasets = {
        'customers': 'olist_customers_dataset.csv',
        'geolocation': 'olist_geolocation_dataset.csv',
        'order_items': 'olist_order_items_dataset.csv',
        'order_payments': 'olist_order_payments_dataset.csv',
        'order_reviews': 'olist_order_reviews_dataset.csv',
        'orders': 'olist_orders_dataset.csv',
        'products': 'olist_products_dataset.csv',
        'sellers': 'olist_sellers_dataset.csv',
        'product_category': 'product_category_name_translation.csv'
    }

    data = {}
    for name, filename in datasets.items():
        path = os.path.join(data_dir, filename)
        if os.path.exists(path):
            data[name] = pd.read_csv(path)
            print(f'Chargé : {name} ({data[name].shape[0]} lignes)')
        else:
            print(f'Attention : Le fichier {path} n\'existe pas.')
            data[name] = None

    return data
