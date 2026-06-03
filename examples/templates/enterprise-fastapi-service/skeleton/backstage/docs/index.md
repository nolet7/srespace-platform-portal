# ${{ values.name }}

## Overview

`${{ values.name }}` is an enterprise FastAPI service generated from the SRESpace Backstage golden-path template.

## Ownership

| Field | Value |
|---|---|
| Owner | ${{ values.owner }} |
| Lifecycle | development |
| System | ${{ values.system }} |
| Repository | nolet7/${{ values.name }} |

## Service Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Service information |
| `/health` | Liveness check |
| `/ready` | Readiness check |
| `/metrics` | Prometheus metrics |

## Platform Standards

This service includes:

- FastAPI application structure
- Dockerfile
- Kubernetes manifests
- Backstage catalog metadata
- TechDocs documentation
- SRE runbook
- SLO documentation
