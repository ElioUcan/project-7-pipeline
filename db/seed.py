import random
import psycopg2
from faker import Faker
from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv()
fake = Faker()


status_code = [200, 400, 404, 500]
endpoints= ["/api", "/", "/api/general"]
api_method = ["GET", "POST", "PUT", "DELETE"]
dag_name = ["pipe_ml", "pipe_finance", "pipe_general"]
status = ["success", "failed"]
duration = random.uniform(1.0, 10.5)

#api_requests table connection with false data
with psycopg2.connect(host=os.getenv("POSTGRES_HOST_LOCAL"),port=5432,database=os.getenv("POSTGRES_DB"),user=os.getenv("POSTGRES_USER"),password=os.getenv("POSTGRES_PASSWORD")) as conn:
    with conn.cursor() as cur:
        for _ in range(100):
            row = (random.choice(endpoints),random.choice(api_method) ,random.choice(status_code),random.uniform(0.1,5.5), fake.date_time())

            cur.execute("INSERT INTO api_requests (endpoint, method, status_code, response_time_ms, requested_at) VALUES (%s, %s, %s, %s, %s);", row)

#pipeline_runs table connection with false data     
with psycopg2.connect(host=os.getenv("POSTGRES_HOST_LOCAL"),port=5432,database=os.getenv("POSTGRES_DB"),user=os.getenv("POSTGRES_USER"),password=os.getenv("POSTGRES_PASSWORD")) as conn:
    with conn.cursor() as cur:
        for _ in range(100):
            row = (random.choice(dag_name), fake.date_time(),fake.date_time()+ timedelta(seconds=duration),random.uniform(1.0,10.5), random.choice(status), random.randint(1,5), fake.date_time())

            cur.execute("INSERT INTO pipeline_runs (dag_name, started_at, end_at,duration,status,retries,created_at) VALUES (%s, %s, %s, %s, %s, %s,%s);", row)
       
#model_inference table connection with false data
with psycopg2.connect(host=os.getenv("POSTGRES_HOST_LOCAL"),port=5432,database=os.getenv("POSTGRES_DB"),user=os.getenv("POSTGRES_USER"),password=os.getenv("POSTGRES_PASSWORD")) as conn:
    with conn.cursor() as cur:
        for _ in range(100):
            row = (fake.name(),random.choice(["healthy", "degraded", "critical"]) ,random.uniform(0.1,5.5), random.choice(status), fake.date_time())

            cur.execute("INSERT INTO model_inference (model_name, label, latency_ms, status, requested_at) VALUES (%s, %s, %s, %s, %s);", row)
       