# DevSecOps Controls

## Purpose

This document defines the DevSecOps controls included in the Full-Stack PostgreSQL Golden Path template.

The goal is to ensure every generated application includes security checks early in the development lifecycle.

## DevSecOps Objectives

- Detect secrets before code is merged
- Detect vulnerable dependencies
- Detect insecure application code
- Detect insecure containers
- Detect insecure Kubernetes manifests
- Detect risky infrastructure-as-code
- Improve supply chain security
- Support audit and compliance evidence

## CI/CD Security Gates

| Gate | Purpose | Recommended Tool |
|---|---|---|
| Secret scanning | Detect committed credentials | Gitleaks |
| SAST | Detect insecure code patterns | Semgrep |
| Dependency scanning | Detect vulnerable packages | Snyk, Dependabot, pip-audit, npm audit |
| Container scanning | Detect image vulnerabilities | Trivy |
| IaC scanning | Detect insecure Terraform/Kubernetes config | Checkov, tfsec |
| SBOM generation | Produce software bill of materials | Syft, Trivy |
| Image signing | Verify trusted images | Cosign |
| Policy validation | Enforce Kubernetes standards | Kyverno, OPA Gatekeeper |

## Required CI/CD Controls

Every repository should include:

- Pull request validation
- Unit tests
- Secret scanning
- SAST scanning
- Dependency scanning
- Container image scanning
- Infrastructure-as-code scanning
- Build artifact validation
- Deployment approval for production
- Rollback evidence

## Secret Management Standard

Do not store secrets in:

- Git repositories
- Dockerfiles
- Helm values files
- Kubernetes plain-text manifests
- Application source code
- CI/CD logs

Use approved secret systems:

- HashiCorp Vault
- External Secrets Operator
- Sealed Secrets
- GitHub Actions secrets
- Kubernetes secrets generated from approved automation

## Container Security Standard

Containers should:

- Run as non-root
- Avoid privileged mode
- Use minimal base images
- Define resource requests and limits
- Avoid unnecessary packages
- Avoid hardcoded secrets
- Use pinned image versions where possible
- Be scanned before deployment
- Be signed where required

## Kubernetes Security Standard

Kubernetes workloads should include:

- Readiness probes
- Liveness probes
- Resource requests
- Resource limits
- Non-root security context
- Least-privilege service account
- NetworkPolicy where applicable
- No privileged containers
- No hostPath unless approved
- No hostNetwork unless approved

## Example Security Context

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop:
      - ALL
Example Resource Limits
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 512Mi
Supply Chain Security

Recommended controls:

Generate SBOM
Scan container image
Sign image with Cosign
Verify image signature before deployment
Restrict unsigned images using admission policy
Track image digest instead of only tag
Use trusted base images
Policy Enforcement

Recommended policy tools:

Kyverno
OPA Gatekeeper

Example policies:

Require non-root containers
Block privileged containers
Require resource limits
Require image registry allowlist
Require signed images
Block latest tag in production
Require labels and ownership metadata
Production Security Checklist

Before production, confirm:

Secret scan completed
SAST scan completed
Dependency scan completed
Container scan completed
IaC scan completed
Kubernetes policy checks passed
SBOM generated
Image signed where required
Secrets injected securely
RBAC reviewed
Resource limits configured
Logs checked for sensitive data
Rollback procedure tested

