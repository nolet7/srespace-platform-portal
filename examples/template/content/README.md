# ${{ values.serviceName }}

${{ values.description }}

## Features

- FastAPI application
- Health and readiness endpoints
- Prometheus metrics endpoint
- Dockerfile
- GitHub Actions CI pipeline
- Helm chart
- Kubernetes manifests
- Backstage catalog file
- TechDocs documentation
- Pytest test structure

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --host 0.0.0.0 --port ${{ values.port }}
```

## Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Service root |
| `/healthz` | Liveness check |
| `/readyz` | Readiness check |
| `/metrics` | Prometheus metrics |

## Docker

```bash
docker build -t ${{ values.serviceName }}:local .
docker run -p ${{ values.port }}:${{ values.port }} ${{ values.serviceName }}:local
```

## Helm

```bash
helm upgrade --install ${{ values.serviceName }} ./helm -n ${{ values.namespace }} --create-namespace
```
