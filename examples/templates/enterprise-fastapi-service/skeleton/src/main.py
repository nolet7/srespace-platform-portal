from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI(
title="${{ values.name }}",
description="${{ values.description }}",
version="1.0.0",
)

REQUEST_COUNT = Counter(
"app_requests_total",
"Total number of requests served by the application",
["endpoint"],
)

@app.get("/")
def root():
REQUEST_COUNT.labels(endpoint="/").inc()
return {
"service": "${{ values.name }}",
"status": "running",
"owner": "${{ values.owner }}",
"lifecycle": "${{ values.lifecycle }}",
}

@app.get("/health")
def health():
REQUEST_COUNT.labels(endpoint="/health").inc()
return {"status": "healthy"}

@app.get("/ready")
def ready():
REQUEST_COUNT.labels(endpoint="/ready").inc()
return {"status": "ready"}

@app.get("/metrics")
def metrics():
REQUEST_COUNT.labels(endpoint="/metrics").inc()
return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
