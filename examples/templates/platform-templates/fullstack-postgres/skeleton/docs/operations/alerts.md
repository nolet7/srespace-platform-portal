# Alerting Guide

## Purpose

This document defines standard alerting rules for applications generated from the Full-Stack PostgreSQL Golden Path template.

## Alerting Goals

Alerts should help the team detect:

- Service outages
- High error rates
- High latency
- Pod failures
- Database connection issues
- Resource saturation
- Deployment failures
- Ingress or routing problems

## Recommended Alert Severity Levels

| Severity | Meaning | Example |
|---|---|---|
| critical | User-facing outage or major service degradation | API unavailable |
| warning | Service is degraded but still usable | p95 latency above target |
| info | Non-urgent operational signal | Deployment completed |

## Critical Alerts

### Service Down

Trigger when the service is not responding.

```promql
up{job="${{ values.component_id }}"} == 0
Recommended duration:

for: 2m
High 5xx Error Rate

Trigger when server-side errors are above acceptable threshold.

(
  sum(rate(http_requests_total{job="${{ values.component_id }}",status=~"5.."}[5m]))
  /
  sum(rate(http_requests_total{job="${{ values.component_id }}"}[5m]))
) > 0.01

Recommended duration:

for: 5m
Deployment Unavailable

Trigger when Kubernetes reports unavailable replicas.

kube_deployment_status_replicas_unavailable{deployment=~"${{ values.component_id }}.*"} > 0

Recommended duration:

for: 5m
Pod CrashLooping

Trigger when pods restart repeatedly.

increase(kube_pod_container_status_restarts_total{pod=~"${{ values.component_id }}.*"}[10m]) > 3

Recommended duration:

for: 5m
Warning Alerts
High Latency

Trigger when p95 latency is above target.

histogram_quantile(
  0.95,
  sum(rate(http_request_duration_seconds_bucket{job="${{ values.component_id }}"}[5m])) by (le)
) > 0.3

Recommended duration:

for: 10m
High CPU Usage

Trigger when CPU usage is consistently high.

sum(rate(container_cpu_usage_seconds_total{pod=~"${{ values.component_id }}.*"}[5m])) by (pod) > 0.8

Recommended duration:

for: 10m
High Memory Usage

Trigger when memory usage is high.

container_memory_working_set_bytes{pod=~"${{ values.component_id }}.*"} > 500000000

Recommended duration:

for: 10m
Pod Not Ready

Trigger when a pod is running but not ready.

kube_pod_status_ready{pod=~"${{ values.component_id }}.*",condition="true"} == 0

Recommended duration:

for: 5m
Database Alerts
PostgreSQL Pod Down
up{job=~".*postgres.*"} == 0
Database Connection Errors

Use application metrics or logs to alert on repeated database connection failures.

Example log query for Loki:

{app="${{ values.component_id }}"} |= "database" |= "connection" |= "error"
Alert Response Process

When an alert fires:

Confirm the alert in Grafana or Alertmanager.
Check application health endpoint.
Check Kubernetes pods.
Check recent deployments.
Review application logs.
Check database connectivity.
Roll back if the issue started after a deployment.
Document the incident.
Useful Commands
kubectl get pods -n dev | grep ${{ values.component_id }}
kubectl get svc -n dev | grep ${{ values.component_id }}
kubectl get ingress -n dev
kubectl logs -n dev deploy/${{ values.component_id }}-api --tail=100
kubectl get events -n dev --sort-by=.lastTimestamp
argocd app get ${{ values.component_id }}

