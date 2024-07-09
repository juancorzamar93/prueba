        
from sqlalchemy import create_engine
from parameters import REDSHIFT_USERNAME, REDSHIFT_PASSWORD, REDSHIFT_HOST, REDSHIFT_DB, REDSHIFT_PORT, REDSHIFT_TABLE

def create_table():
    try:
        conn_str = f'postgresql+psycopg2://{REDSHIFT_USERNAME}:{REDSHIFT_PASSWORD}@{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DB}'
        engine = create_engine(conn_str)

        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {REDSHIFT_TABLE}(
            currency VARCHAR,
            rate FLOAT,
            base VARCHAR,
            date DATE,
            timestamp TIMESTAMP,
            ingestion_time TIMESTAMP,
            PRIMARY KEY (date, currency)
        );
        """

        with engine.connect() as connection:
            connection.execute(create_table_query)
        print("Tabla creada exitosamente en Redshift")
    except Exception as e:
        print(f"Error al crear la tabla en Redshift: {e}")
