# Usa la imagen oficial de Python como base
FROM apache/airflow:2.9.2

# Establece el directorio de trabajo
WORKDIR /usr/local/airflow

# Establece las variables de entorno necesarias para Apache Airflow
ENV AIRFLOW_HOME=/usr/local/airflow

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libblas-dev \
    liblapack-dev \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala Apache Airflow
RUN pip install apache-airflow==2.9.2 -r requirements.txt

# Copia el archivo .env al contenedor
COPY .env /opt/airflow/.env

# Copia los archivos del DAG y los módulos al contenedor
COPY dags / $AIRFLOW_HOME/dags/
COPY requirements.txt $AIRFLOW_HOME/requirements.txt

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r $AIRFLOW_HOME/requirements.txt

# Inicializa la base de datos de Airflow
RUN airflow db init

# Copia el archivo de configuración de Airflow (si tienes uno)
# COPY airflow.cfg $AIRFLOW_HOME/airflow.cfg

# Establece el comando por defecto para ejecutar el scheduler y el webserver
CMD ["sh", "-c", "airflow scheduler & airflow webserver"]


