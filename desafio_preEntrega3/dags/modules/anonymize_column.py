import hashlib

def anonymize_column(df):
    try:
        # Anonimizar la columna 'base' usando hashlib
        df['base'] = df['base'].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())
        return df
    except Exception as e:
        print(f"Error al anonimizar la columna 'base': {e}")
        return None
