# Architecture

## High-Level Flow

```text
Client
  |
  v
FastAPI Service
  |
  v
/healthz /readyz /metrics
  |
  v
Prometheus / Kubernetes / Backstage
```

## Main Components

- FastAPI application
- Container image
- Helm chart
- Kubernetes deployment
- Backstage catalog metadata
- TechDocs documentation
