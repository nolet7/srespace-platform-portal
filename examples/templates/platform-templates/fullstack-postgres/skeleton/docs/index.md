# ${{ values.component_id }}

${{ values.description }}

## Overview

This service was generated from the **Full-Stack PostgreSQL Golden Path** Backstage template.

The template is designed for enterprise platform engineering, DevOps, DevSecOps, Kubernetes delivery, observability, and documentation.

## Included Capabilities

- Frontend application starter
- Backend API starter
- PostgreSQL database pattern
- Dockerfile
- GitHub Actions CI/CD workflow
- Helm chart
- Argo CD GitOps application
- Prometheus alert starter
- Grafana dashboard notes
- DevSecOps controls
- Kubernetes policy examples
- SRE runbooks
- TechDocs documentation

## Standard Delivery Flow

```text
Developer
  → Backstage Template
  → GitHub Repository
  → CI/CD Pipeline
  → Docker Image
  → Helm Chart
  → Argo CD
  → Kubernetes
  → Prometheus/Grafana
  → TechDocs
Ownership

Owner:

${{ values.owner }}
Environment Strategy

Recommended environments:

dev
devops
production
Recommended Platform Tools
Area	Tools
Developer Portal	Backstage, Software Catalog, Scaffolder, TechDocs
Source Control	GitHub
CI/CD	GitHub Actions, Jenkins, Tekton
Containers	Docker
Kubernetes Delivery	Helm, Kustomize, Argo CD, Flux
Infrastructure	Terraform, OpenTofu, Crossplane
Secrets	Vault, External Secrets Operator, Sealed Secrets
Observability	Prometheus, Grafana, Loki, Tempo, OpenTelemetry
Security	Trivy, Semgrep, Gitleaks, Checkov, tfsec
Policy	Kyverno, OPA Gatekeeper
Supply Chain	SBOM, Cosign
Runtime Security	Falco
Quality	Pytest, Jest, ESLint, SonarQube/SonarCloud

