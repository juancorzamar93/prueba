
CREATE TABLE exchange_rate_data(
            currency VARCHAR,
            rate FLOAT,
            base VARCHAR,
            date DATE,
            timestamp TIMESTAMP,
            ingestion_time TIMESTAMP,
            PRIMARY KEY (date, currency)
        );