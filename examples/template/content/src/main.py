from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

SERVICE_NAME = "${{ values.serviceName }}"

app = FastAPI(
    title=SERVICE_NAME,
    description="${{ values.description }}",
    version="1.0.0",
)

Instrumentator().instrument(app).expose(app)


@app.get("/")
def root():
    return {
        "service": SERVICE_NAME,
        "status": "running",
        "owner": "${{ values.owner }}",
        "lifecycle": "${{ values.lifecycle }}",
    }


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/readyz")
def readyz():
    return {"status": "ready"}
