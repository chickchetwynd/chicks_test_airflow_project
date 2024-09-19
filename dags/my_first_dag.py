from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'Chick',
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    'chicks_first_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as chicks_first_dag:
    
    task1 = BashOperator(
        task_id='task1',
        bash_command = 'echo "Hello World!"'
    )

    task2 = BashOperator(
        task_id = 'task2',
        bash_command = 'echo "Hello Again!"'
    )

    task1 >> task2