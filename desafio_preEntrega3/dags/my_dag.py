# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from datetime import datetime, timedelta
# import os
# from modules.load_data import load_data
# from modules.data_transformation import transform_data
# from modules.extract_data import extract_data
# from modules.create_table import create_table
# from modules.validate_credentials import validate_credentials
# from modules.clean_and_transformation import clean_data
# from modules.anonymize_column import anonymize_column
# from parameters import API_URL
# from dotenv import load_dotenv

# load_dotenv()

# def main():
#     if not validate_credentials():
#         return

#     create_table()
#     data = extract_data(API_URL)
#     if data:
#         transformed_data = transform_data(data)
#         if transformed_data is not None:
#             cleaned_data = clean_data(transformed_data)
#             if cleaned_data is not None:
#                 anonymized_data = anonymize_column(cleaned_data)
#                 if anonymized_data is not None:
#                     load_data(anonymized_data)


# default_args = {
#     'owner': 'juan_ml',
#     'depends_on_past': False,
#     'start_date': datetime(2024, 1, 1),
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# dag = DAG(
#     'exchange_rate_dag',
#     default_args=default_args,
#     description='DAG para extraer, transformar y cargar datos de tasas de cambio',
#     schedule_interval=timedelta(days=1),
# )

# run_script = PythonOperator(
#     task_id='run_script',
#     python_callable=main,
#     dag=dag,
# )

# run_script

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from modules.create_table import create_table
from modules.validate_credentials import validate_credentials
from modules.extract_data import extract_data
from modules.data_transformation import transform_data
from modules.clean_and_transformation import clean_data
from modules.load_data import load_data
from parameters import API_URL
from dotenv import load_dotenv

load_dotenv()

default_args = {
    'owner': 'juan_ml',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'exchange_rate_dag',
    default_args=default_args,
    description='DAG para extraer, transformar y cargar datos de tasas de cambio',
    schedule_interval=timedelta(days=1),
)

# def main():
#     if not validate_credentials():
#         return

#     create_table()

def main():
    if not validate_credentials():
        print("Invalid credentials. Exiting...")
        return

    try:
        create_table()
        data = extract_data(API_URL)
        if data:
            transformed_data = transform_data(data)
            cleaned_data = clean_data(transformed_data)
            anonymized_data = anonymize_column(cleaned_data)
            load_data(anonymized_data)
    except Exception as e:  # Catch all exceptions for broad error handling
        print(f"An error occurred during data processing: {e}")


with dag:
    task_create_table = PythonOperator(
        task_id='create_table',
        python_callable=create_table
    )

    task_extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )

    task_transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    task_load = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    task_create_table >> task_extract >> task_transform >> task_load
