# ML Pipeline Monitoring API

A containerized observability platform for tracking ML pipeline runs, model inference metrics, and API health — with a live Grafana dashboard backed by PostgreSQL.

## Overview

This project exposes a FastAPI service that records and queries operational data across three domains:

- **Pipeline runs** — DAG execution history with status, duration, and retry counts
- **Model inference** — prediction labels, latency, and status per model
- **API health** — per-endpoint request logs with response times and status codes

Grafana connects directly to the database to render real-time charts for each domain.

## Architecture

```
┌──────────┐     ┌─────────────┐     ┌──────────────┐
│  Client  │────▶│  FastAPI    │────▶│  PostgreSQL   │
└──────────┘     │  (port 5600)│     │  (port 5432)  │
                 └─────────────┘     └──────┬───────┘
                                            │
                 ┌─────────────┐            │
                 │   Grafana   │────────────┘
                 │  (port 3000)│
                 └─────────────┘
```

**Services (Docker Compose)**

| Service     | Image / Build | Role                                      |
|-------------|---------------|-------------------------------------------|
| `db`        | postgres:15   | Primary data store                        |
| `app`       | `./app`       | FastAPI REST API                          |
| `dashboard` | grafana/grafana | Visualization layer                     |
| `seeder`    | `./db`        | One-shot seed job to populate sample data |

Networks: `frontend` (app ↔ dashboard) and `backend` (app ↔ db ↔ seeder).

## API Reference

All routes are prefixed with `/api/v1` and require a Bearer token.

### Authentication

```
POST /api/v1/auth/token
```

Request body:
```json
{ "username": "admin", "password": "secret" }
```

Response:
```json
{ "access_token": "<jwt>", "token_type": "bearer" }
```

Token expires in 30 minutes (HS256).

---

### Pipeline Runs

```
GET /api/v1/pipelines?hours=24
```

Returns all rows from `pipeline_runs` within the last `hours` hours.

| Field        | Type      | Description                      |
|-------------|-----------|----------------------------------|
| `dag_name`  | string    | Name of the DAG                  |
| `started_at`| timestamp | Run start time                   |
| `end_at`    | timestamp | Run end time                     |
| `duration`  | int       | Duration in seconds              |
| `status`    | string    | `success` / `failed` / etc.      |
| `retries`   | int       | Number of retries                |

---

### Model Inference

```
GET /api/v1/inference?hours=24
```

Returns all rows from `model_inference` within the last `hours` hours.

| Field          | Type      | Description                   |
|---------------|-----------|-------------------------------|
| `model_name`  | string    | Model identifier              |
| `label`       | string    | Predicted label               |
| `latency_ms`  | float     | Inference latency (ms)        |
| `status`      | string    | `success` / `error`           |
| `requested_at`| timestamp | Request timestamp             |

---

### API Health

```
GET /api/v1/health
```

Returns the health status of the API.

## Database Schema

Three tables are initialized via `db/init.sql` on first container start:

```sql
pipeline_runs   -- DAG execution records
model_inference -- Model prediction records
api_requests    -- HTTP request logs
```

Sample data is inserted by the `seeder` service using `db/seed.py`.

## Getting Started

### Prerequisites

- Docker & Docker Compose

### Configuration

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

```env
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_PORT=
```

### Run

```bash
docker compose up --build
```

| Service   | URL                      |
|-----------|--------------------------|
| API       | http://localhost:5600     |
| API Docs  | http://localhost:5600/docs|
| Grafana   | http://localhost:3000     |

The seeder runs once on startup and populates the database with synthetic data.

## Tech Stack

- **FastAPI** — REST API framework
- **SQLAlchemy** — Database ORM
- **PostgreSQL 15** — Relational database
- **Grafana** — Dashboard and visualization
- **Docker Compose** — Container orchestration
- **python-jose** — JWT authentication
