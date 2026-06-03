# CI/CD

## Pipeline Overview

This service includes an enterprise GitHub Actions workflow.

## Pipeline Stages

| Stage | Purpose |
|---|---|
| Install dependencies | Validate Python runtime dependencies |
| Validate TechDocs | Confirm documentation builds successfully |
| Build Docker image | Confirm container image builds |
| Helm lint | Validate Helm chart structure |
| Helm template | Render Kubernetes manifests |
| DockerHub push | Push image on main branch |

## Required GitHub Secrets

Configure these repository secrets before pushing production images:

| Secret | Purpose |
|---|---|
| `DOCKERHUB_USERNAME` | DockerHub username |
| `DOCKERHUB_TOKEN` | DockerHub access token |

## Image Tagging

The workflow pushes two tags:

```text
latest
short-commit-sha
Example:

noletengine/payment-service:latest
noletengine/payment-service:a1b2c3d
Validation Commands

Run locally:

mkdocs build --strict --site-dir /tmp/techdocs-site
docker build -t local-service:ci .
helm lint ./helm
helm template service-name ./helm

