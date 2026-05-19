FROM python:3.12-slim


WORKDIR /app

COPY requirementsApp.txt .

RUN pip install -r requirementsApp.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5600"]