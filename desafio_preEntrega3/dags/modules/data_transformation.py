
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

# import json
# import pandas as pd

# def transform_data():
#     with open('/tmp/extracted_data.json', 'r') as f:
#         data = json.load(f)
    
#     try:
#         rates = data.get('rates', {})
#         timestamp = pd.to_datetime(data.get('timestamp'), unit='s')
#         df = pd.DataFrame(rates.items(), columns=['currency', 'rate'])
#         df['base'] = data.get('base')
#         df['date'] = data.get('date')
#         df['timestamp'] = timestamp
#         df['ingestion_time'] = pd.Timestamp.now()
        
#         # Guardar los datos transformados
#         df.to_csv('/tmp/transformed_data.csv', index=False)
#         return df
#     except Exception as e:
#         print(f"Error al transformar los datos: {e}")
#         return None
