from datetime import datetime, timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

# Dictionary to set the default arguments for each operator
# There are lots more options, please read the Airflow Documents
default_args = {
    'owner': 'muict building',  # Change this to be your name
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

# Start defining DAG
with DAG(
    dag_id='workflow',  # Unique ID
    default_args=default_args,  # Default Arguments
    description='pipeline of data engineer process',  # Description
    start_date=datetime(2024, 1, 23, 2),  # When to start this workflow (DAG)
    schedule_interval='@daily'            # Repeat the workflow every day
) as dag:

		# This is the first task inside the DAG workflow
    task1 = BashOperator(
        task_id='Extract',
        bash_command="echo extracting data from API"
    )
    task2 = BashOperator(
        task_id='Load',
        bash_command="echo Load data to storage"
    )

    task3 = BashOperator(
        task_id='Transform',
        bash_command="echo Transform into 3 tier of using data"
    )

# Workflow dependency
# Since there is only one task, you simply add the task1 object here
task1 >> task2 >> task3