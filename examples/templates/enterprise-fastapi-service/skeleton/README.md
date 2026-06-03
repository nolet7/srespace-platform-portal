# ${{ values.name }}

${{ values.description }}

## Service Overview

This service was generated using the SRESpace enterprise Backstage golden-path template.

## Capabilities

- FastAPI application
- Docker container build
- Kubernetes deployment manifest
- GitHub Actions CI workflow
- Backstage catalog metadata
- TechDocs documentation
- SRE runbook
- SLO documentation

## Local Run

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
uvicorn src.main:app --host 0.0.0.0 --port ${{ values.servicePort }}
Health Check
curl http://localhost:${{ values.servicePort }}/health

