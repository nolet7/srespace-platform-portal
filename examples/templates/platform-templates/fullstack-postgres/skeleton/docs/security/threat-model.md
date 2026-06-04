# Threat Model

## Purpose

This document identifies common security risks for applications generated from the Full-Stack PostgreSQL Golden Path template.

## System Scope

The application includes:

- Frontend web application
- Backend API service
- PostgreSQL database
- Kubernetes workloads
- Ingress routing
- CI/CD pipeline
- Container images
- Secrets and configuration
- Observability components
- Documentation and runbooks

## Key Assets

| Asset | Why It Matters |
|---|---|
| Source code | Contains business logic and application behavior |
| Container images | Runs production workload |
| PostgreSQL data | Stores application data |
| API endpoints | Exposes business functionality |
| Secrets | Protects credentials and tokens |
| CI/CD pipeline | Builds and deploys application |
| Kubernetes manifests | Defines runtime behavior |
| Observability data | Contains logs, metrics, and traces |

## Common Threats

| Threat | Risk | Control |
|---|---|---|
| Hardcoded secrets | Credential exposure | Use Vault, External Secrets, or sealed secrets |
| Vulnerable dependencies | Exploitable packages | Use dependency scanning |
| Insecure container image | Runtime compromise | Use Trivy scanning |
| Privileged container | Cluster compromise | Run as non-root |
| Excessive RBAC | Unauthorized access | Apply least privilege |
| Insecure ingress | Data exposure | Use TLS and approved ingress rules |
| Missing resource limits | Noisy neighbor impact | Define CPU and memory limits |
| Weak CI/CD controls | Unsafe deployments | Use approval gates and scans |
| Unsigned images | Supply chain risk | Use Cosign image signing |
| Missing audit logs | Poor incident response | Enable logs and audit trails |

## Trust Boundaries

```text
User Browser
  ↓
Ingress Boundary
  ↓
Frontend Service
  ↓
API Service Boundary
  ↓
Database Boundary
  ↓
Kubernetes Platform Boundary
Required Security Controls
No hardcoded secrets
Secret scanning in CI/CD
SAST scanning
Dependency scanning
Container image scanning
IaC scanning
Non-root container execution
Resource requests and limits
Kubernetes NetworkPolicy where applicable
Least-privilege RBAC
Secure secret management
TLS for external traffic
Audit logging
Rollback capability
DevSecOps Tool Mapping
Control AreaRecommended Tool
Secret scanningGitleaks
SASTSemgrep
Dependency scanningSnyk, Dependabot, npm audit, pip-audit
Container scanningTrivy
IaC scanningCheckov, tfsec
Policy enforcementKyverno, OPA Gatekeeper
Image signingCosign
SBOMSyft, Trivy
Runtime detectionFalco
Secrets managementVault, External Secrets Operator
Production Security Checklist

Before production, confirm:

No secrets are committed to Git
CI/CD security scans run successfully
Container image has been scanned
Kubernetes manifests pass policy checks
Application runs as non-root
Resource limits are configured
Ingress uses approved routing
Secrets are injected securely
RBAC is limited to required permissions
Logs do not expose sensitive data
Rollback procedure exists
Owner is defined in Backstage

