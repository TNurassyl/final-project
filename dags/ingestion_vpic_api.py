from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import psycopg2


API_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json"


def load_vpic_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()["Results"]

    conn = psycopg2.connect(
        host="postgres",
        dbname="airflow",
        user="airflow",
        password="airflow"
    )
    cur = conn.cursor()

    # idempotency
    cur.execute("DELETE FROM raw.vehicle_types;")
    cur.execute("DELETE FROM raw.manufacturers;")

    now = datetime.utcnow()

    for row in data:
        cur.execute(
            """
            INSERT INTO raw.manufacturers (mfr_id, mfr_name, country, ingested_at)
            VALUES (%s, %s, %s, %s)
            """,
            (
                row.get("Mfr_ID"),
                row.get("Mfr_Name"),
                row.get("Country"),
                now
            )
        )

        for vt in row.get("VehicleTypes", []):
            cur.execute(
                """
                INSERT INTO raw.vehicle_types (mfr_id, vehicle_type, ingested_at)
                VALUES (%s, %s, %s)
                """,
                (
                    row.get("Mfr_ID"),
                    vt.get("Name"),
                    now
                )
            )

    conn.commit()
    cur.close()
    conn.close()


with DAG(
    dag_id="ingestion_vpic_api",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["ingestion", "raw"]
) as dag:

    load_data = PythonOperator(
        task_id="load_vpic_data",
        python_callable=load_vpic_data
    )
