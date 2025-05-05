from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

with DAG('snowflake_dbt_pipeline',
         start_date=days_ago(1),
         schedule_interval='@daily',
         catchup=False) as dag:

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /usr/local/airflow/dbt && dbt run'
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /usr/local/airflow/dbt && dbt test'
    )

    dbt_run >> dbt_test
