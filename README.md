# ML Pipeline Monitoring API

## 🛠️ Technologies
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## ✨ Features
- Track pipeline run history: DAG name, status, duration, and retry count
- Log model inference records: prediction label, latency, and per-model status
- Monitor API health: per-endpoint request logs with response times and status codes
- JWT authentication (HS256, 30-minute token expiration) on all routes
- Live Grafana dashboard connected directly to PostgreSQL for real-time charts
- One-shot seeder service that populates the database with synthetic data on startup

## 🎯 Uses
Observability platform for ML systems, demonstrating how to track pipeline execution, model performance, and API health in a single dashboard. Built as project #7 in a Data/AI/MLOps engineering portfolio to show production-level monitoring patterns.

## 🔧 Process
FastAPI exposes REST endpoints under `/api/v1` that write and query operational data across three PostgreSQL tables. Grafana connects directly to the database for low-latency chart rendering. Docker Compose orchestrates four services: `db`, `app`, `dashboard`, and `seeder`. The `seeder` runs once on startup to populate sample data, so the dashboard is functional immediately after `docker compose up`.

## 💡 Learnings
- Designing metrics schemas for ML observability (separating pipeline, inference, and API concerns into distinct tables)
- JWT authentication with FastAPI's dependency injection system
- Connecting Grafana directly to PostgreSQL as a datasource instead of building a separate metrics API
- Using Docker Compose network segmentation (`frontend` / `backend`) to control service visibility

## ▶️ Running the project

```bash
cp .env.example .env
# fill in POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_PORT
docker compose up --build
```

| Service | URL |
|---------|-----|
| API | http://localhost:5600 |
| API Docs | http://localhost:5600/docs |
| Grafana | http://localhost:3000 |
