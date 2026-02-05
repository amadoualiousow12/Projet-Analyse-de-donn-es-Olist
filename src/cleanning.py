import pandas as pd

def cleaning(data):
    """Nettoie les données Olist."""
    # 1. Nettoyage Customers
    if data['customers'] is not None:
        data['customers'] = data['customers'].drop_duplicates(subset=['customer_unique_id'], keep='first')

    # 2. Nettoyage Orders
    if data['orders'] is not None:
        date_cols = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
                     'order_delivered_customer_date', 'order_estimated_delivery_date']
        for col in date_cols:
            data['orders'][col] = pd.to_datetime(data['orders'][col], errors='coerce')

    # 3. Nettoyage Products
    if data['products'] is not None:
        data['products']['product_category_name'] = data['products']['product_category_name'].fillna('unknown')
        num_cols = ['product_name_lenght', 'product_description_lenght', 'product_photos_qty',
                    'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
        data['products'][num_cols] = data['products'][num_cols].fillna(0)

    # 4. Nettoyage Reviews
    if data['order_reviews'] is not None:
        data['order_reviews']['review_comment_title'] = data['order_reviews']['review_comment_title'].fillna('No Title')
        data['order_reviews']['review_comment_message'] = data['order_reviews']['review_comment_message'].fillna('No Comment')
        data['order_reviews'] = data['order_reviews'].drop_duplicates(subset=['review_id'], keep='first')

    # 5. Nettoyage Order Items
    if data['order_items'] is not None:
        data['order_items']['shipping_limit_date'] = pd.to_datetime(data['order_items']['shipping_limit_date'])

    # 6. Nettoyage Payments
    if data['order_payments'] is not None:
        data['order_payments'] = data['order_payments'].drop_duplicates()

    # 7. Nettoyage Sellers
    if data['sellers'] is not None:
        data['sellers'] = data['sellers'].drop_duplicates(subset=['seller_id'])

    # 8. Nettoyage Geolocation
    if data['geolocation'] is not None:
        geo = data['geolocation'].drop_duplicates()
        geo = geo.dropna(subset=['geolocation_lat', 'geolocation_lng'])
        data['geolocation'] = geo.groupby('geolocation_zip_code_prefix').agg({
            'geolocation_lat': 'median',
            'geolocation_lng': 'median',
            'geolocation_city': 'first',
            'geolocation_state': 'first'
        }).reset_index()

    print('Nettoyage terminé.')
    return data
