from fastapi import FastAPI
from routers import pipelines, inference, api_health

app = FastAPI()

app.include_router(pipelines.router, prefix="/api/v1", tags=["pipelines"])
app.include_router(inference.router, prefix="/api/v1", tags=["inference"])
app.include_router(api_health.router, prefix="/api/v1", tags=["api-health"])