# Security

## Overview

This service includes baseline container and Kubernetes security controls.

## Included Security Controls

| Control | Purpose |
|---|---|
| Non-root container user | Prevents the application from running as root |
| Dropped Linux capabilities | Reduces container privilege |
| allowPrivilegeEscalation: false | Blocks privilege escalation |
| seccomp RuntimeDefault | Uses the default secure syscall profile |
| Resource limits | Reduces blast radius from runaway processes |
| Trivy scan | Scans image vulnerabilities in CI/CD |

## CI/CD Security Scan

The GitHub Actions workflow includes a Trivy vulnerability scan after the Docker image build.

## Kubernetes Security Validation

Check deployment security settings:

    kubectl get deploy ${{ values.name }} -n dev -o yaml

Confirm pods are running:

    kubectl get pods -n dev -l app=${{ values.name }}

## Security Notes

For production, review:

- Image signing
- SBOM generation
- Admission control with Kyverno or OPA Gatekeeper
- Secret injection from Vault or external-secrets
- NetworkPolicy restrictions by namespace and service account
