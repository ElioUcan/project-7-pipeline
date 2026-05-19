FROM python:3.12-slim

WORKDIR /app

COPY requirementsDB.txt .

RUN pip install -r requirementsDB.txt

COPY . .

CMD ["python", "seed.py"]