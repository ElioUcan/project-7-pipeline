import random
import psycopg2
from faker import Faker

fake = Faker()

status_code = ["200 OK", "400", "404 Not found", "500 Error server"]
endpoints= ["/api", "/", "/api/general"]
api_method = ["GET", "POST", "PUT", "DELETE"]
dag_name = ["pipe_ml", "pipe_finance", "pipe_general"]
status = ["success", "failedS"]

#api_requests table connection with false data
with psycopg2.connect() as conn:
    with conn.cursor() as cur:
        for _ in range(100):
            row = (random.choice(endpoints),random.choice(api_method) ,random.choice(status_code),random.uniform(0.1,5.5), fake.date_time())

            cur.execute("INSERT INTO api_requests VALUES (%s %s %s %s %s)", row)

#pipeline_runs table connection with false data     
with psycopg2.connect() as conn:
    with conn.cursor() as cur:
        for _ in range(100):
            row = (random.choice(dag_name), fake.date_time(),fake.date_time(),random.uniform(1.0,10.5), random.choice(status), random.randint(1,5))

            cur.execute("INSERT INTO pipeline_runs VALUES (%s %s %s %s %s)", row)
       
#model_inference table connection with false data
with psycopg2.connect() as conn:
    with conn.cursor() as cur:
        for _ in range(100):
            row = (fake.name(),random.choice(["healthy", "degraded", "critical"]) ,random.uniform(0.1,5.5), random.choice(status), fake.timestamp())

            cur.execute("INSERT INTO model_inference VALUES (%s %s %s %s %s)", row)
       