from fastapi import FastAPI
from routers import pipelines, inference, api_health, auth

app = FastAPI()

app.include_router(pipelines.router, prefix="/api/v1", tags=["pipelines"])
app.include_router(inference.router, prefix="/api/v1", tags=["inference"])
app.include_router(api_health.router, prefix="/api/v1", tags=["api-health"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])