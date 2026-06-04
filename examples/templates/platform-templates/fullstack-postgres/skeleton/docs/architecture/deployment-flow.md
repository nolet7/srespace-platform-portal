# Deployment Flow

## Purpose

This document explains how applications generated from this Backstage template move from developer request to Kubernetes deployment.

## End-to-End Flow

```text
Developer
  ↓
Backstage Create Page
  ↓
Golden Path Template
  ↓
GitHub Repository
  ↓
CI/CD Pipeline
  ↓
Docker Image Build
  ↓
Security Scans
  ↓
Image Registry
  ↓
Helm Chart
  ↓
Argo CD Sync
  ↓
Kubernetes Deployment
  ↓
Prometheus, Grafana, Loki
  ↓
TechDocs and Runbooks
Step 1: Developer Creates the Application

The developer opens Backstage and selects the application template.

Example templates:

Full-Stack PostgreSQL Golden Path
FastAPI Service Golden Path
Node.js API Golden Path
React Frontend Golden Path
Worker Service Golden Path
Terraform/OpenTofu Module Golden Path
Observability Golden Path
Step 2: Backstage Generates the Repository

Backstage creates a GitHub repository with:

Application starter code
Dockerfile
GitHub Actions workflow
Helm chart
Argo CD application manifest
TechDocs documentation
SRE runbooks
Security policy examples
Monitoring starter files
Step 3: CI/CD Pipeline Runs

The CI/CD workflow should perform:

Code validation
Unit tests
Secret scanning
Static application security testing
Dependency scanning
Container image build
Container image vulnerability scanning
Infrastructure-as-code scanning
SBOM generation where required
Step 4: Docker Image Is Built

The application is packaged into a container image.

Example image naming:

noletengine/${{ values.component_id }}:latest

Recommended image tags:
latest
commit-sha
semantic-version
environment-tag
Step 5: Security Gates Run

Recommended DevSecOps checks:

Control	Tool
Secret scanning	Gitleaks
SAST	Semgrep
Container scan	Trivy
IaC scan	Checkov or tfsec
Dependency scan	Snyk or Dependabot
Image signing	Cosign
Kubernetes policy	Kyverno or OPA Gatekeeper
Step 6: Helm Chart Defines Kubernetes Resources

The Helm chart should define:

Deployment
Service
Ingress
ConfigMap
Secret reference
Resource requests and limits
Probes
ServiceMonitor where applicable
NetworkPolicy where applicable
Step 7: Argo CD Deploys the Application

Argo CD watches the GitHub repository and syncs the desired state into Kubernetes.

Recommended Argo CD settings:

Auto-sync enabled
Self-heal enabled
Prune enabled
Namespace auto-creation enabled for non-production
Manual approval for production where required
Step 8: Kubernetes Runs the Workload

Kubernetes should manage:

Pod scheduling
Health checks
Rolling updates
Self-healing
Service discovery
Horizontal scaling
Resource enforcement
Step 9: Observability Is Enabled

Recommended observability stack:

Prometheus for metrics
Grafana for dashboards
Loki for logs
Tempo for traces
OpenTelemetry for instrumentation
Step 10: Operations Team Uses Runbooks

Every generated application should include:

Health check runbook
Rollback runbook
Incident response runbook
SLO documentation
Alert documentation
Troubleshooting steps
Production Readiness Checklist

Before production, confirm:

Application starts successfully
Health endpoint works
Readiness and liveness probes exist
Resource requests and limits are configured
Secrets are not hardcoded
CI/CD pipeline passes
Security scans pass or are reviewed
Helm chart renders successfully
Argo CD sync succeeds
Dashboards exist
Alerts exist
Rollback procedure is documented
Owner is defined in Backstage catalog

