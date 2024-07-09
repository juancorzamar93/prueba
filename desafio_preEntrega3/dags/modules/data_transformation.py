import pandas as pd

def transform_data(data):
    try:
        rates = data.get('rates', {})
        timestamp = pd.to_datetime(data.get('timestamp'), unit='s')
        df = pd.DataFrame(rates.items(), columns=['currency', 'rate'])
        df['base'] = data.get('base')
        df['date'] = data.get('date')
        df['timestamp'] = timestamp
        df['ingestion_time'] = pd.Timestamp.now()
        return df
    except Exception as e:
        print(f"Error al transformar los datos: {e}")
        return None

