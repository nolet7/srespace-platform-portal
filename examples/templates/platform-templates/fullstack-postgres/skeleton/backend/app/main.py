from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import time
import os

APP_NAME = "${{ values.component_id }}"

app = FastAPI(
    title=APP_NAME,
    description="${{ values.description }}",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"],
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"],
)

@app.middleware("http")
async def metrics_middleware(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    endpoint = request.url.path
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=endpoint,
        status=response.status_code,
    ).inc()

    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=endpoint,
    ).observe(duration)

    return response

@app.get("/")
def root():
    return {
        "service": APP_NAME,
        "message": "Generated from Backstage Full-Stack PostgreSQL Golden Path",
        "docs": "/docs",
        "health": "/api/health",
        "metrics": "/metrics",
    }

@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "service": APP_NAME,
        "environment": os.getenv("APP_ENV", "dev"),
    }

@app.get("/api/categories")
def categories():
    return [
        {
            "id": 1,
            "name": "Platform Engineering",
            "slug": "platform-engineering",
        },
        {
            "id": 2,
            "name": "DevOps",
            "slug": "devops",
        },
        {
            "id": 3,
            "name": "DevSecOps",
            "slug": "devsecops",
        },
        {
            "id": 4,
            "name": "Observability",
            "slug": "observability",
        },
    ]

@app.get("/api/products")
def products():
    return [
        {
            "id": 1,
            "name": "Backstage Golden Path Template",
            "category": "Platform Engineering",
            "description": "Reusable template for creating production-ready services.",
            "rating": 5,
        },
        {
            "id": 2,
            "name": "Helm and Argo CD Delivery",
            "category": "DevOps",
            "description": "Standard GitOps deployment model for Kubernetes workloads.",
            "rating": 5,
        },
        {
            "id": 3,
            "name": "DevSecOps Security Gates",
            "category": "DevSecOps",
            "description": "Security controls for scanning code, containers, secrets, and IaC.",
            "rating": 5,
        },
        {
            "id": 4,
            "name": "Prometheus and Grafana Starter",
            "category": "Observability",
            "description": "Metrics, dashboards, alerts, and SLO starter package.",
            "rating": 5,
        },
    ]

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
