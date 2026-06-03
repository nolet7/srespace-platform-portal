# Kubernetes Platform

## Purpose

The portal documents Kubernetes standards for service deployment, reliability, and operations.

## Recommended Kubernetes Standards

| Area | Standard |
|---|---|
| Namespace | One namespace per environment or team boundary |
| Probes | Readiness and liveness probes required |
| Resources | CPU and memory requests/limits required |
| Secrets | Use Vault or Kubernetes secrets, never hardcode |
| Ingress | Use managed ingress or approved reverse proxy |
| Observability | Metrics endpoint and logs required |
| Deployment | Helm or GitOps preferred |

## Deployment Baseline

A production workload should include:

- Deployment
- Service
- Ingress or route
- ConfigMap
- Secret reference
- HPA where applicable
- PodDisruptionBudget where applicable
- ServiceMonitor or metrics scrape configuration

## Reliability Controls

- Rolling deployments
- Rollback procedures
- Health checks
- Horizontal scaling
- Resource quotas
- Network policies where required
- Persistent volume backup strategy for stateful services

## Backstage Integration

Kubernetes plugins can help teams view workloads, pods, deployments, and service health from the portal.
