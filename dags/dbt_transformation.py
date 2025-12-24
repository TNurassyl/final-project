from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

DBT_DIR = "/opt/airflow/dbt"

with DAG(
    dag_id="dbt_transformation",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["dbt", "transformation"]
) as dag:

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"""
        pip install --quiet dbt-core dbt-postgres &&
        cd {DBT_DIR} &&
        dbt run
        """
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"""
        pip install --quiet dbt-core dbt-postgres &&
        cd {DBT_DIR} &&
        dbt test
        """
    )

    dbt_run >> dbt_test
