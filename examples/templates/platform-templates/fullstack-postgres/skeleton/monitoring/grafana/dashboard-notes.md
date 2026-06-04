# Grafana Dashboard Starter

## Purpose

This document defines the recommended Grafana dashboard panels for applications generated from the Full-Stack PostgreSQL Golden Path template.

## Dashboard Name

```text
${{ values.component_id }} - SRE Service Overview
Recommended Dashboard Sections
Service Health
Traffic
Errors
Latency
Kubernetes Health
Resource Usage
Database Health
Deployment Status
Panel 1: Service Availability

PromQL:

up{job="${{ values.component_id }}"}

Recommended visualization:

Stat panel

Expected value:

1 = healthy
0 = down
Panel 2: Request Rate

PromQL:

sum(rate(http_requests_total{job="${{ values.component_id }}"}[5m]))

Recommended visualization:

Time series
Panel 3: Error Rate

PromQL:

(
  sum(rate(http_requests_total{job="${{ values.component_id }}",status=~"5.."}[5m]))
  /
  sum(rate(http_requests_total{job="${{ values.component_id }}"}[5m]))
) * 100

Recommended visualization:

Gauge or time series

Thresholds:

Green: below 1%
Yellow: 1% to 5%
Red: above 5%
Panel 4: p95 Latency

PromQL:

histogram_quantile(
  0.95,
  sum(rate(http_request_duration_seconds_bucket{job="${{ values.component_id }}"}[5m])) by (le)
)

Recommended visualization:

Time series

Thresholds:

Green: below 300ms
Yellow: 300ms to 700ms
Red: above 700ms
Panel 5: Pod Restarts

PromQL:

increase(kube_pod_container_status_restarts_total{pod=~"${{ values.component_id }}.*"}[10m])

Recommended visualization:

Bar gauge or time series
Panel 6: Ready Replicas

PromQL:

kube_deployment_status_replicas_ready{deployment=~"${{ values.component_id }}.*"}

Recommended visualization:

Stat panel
Panel 7: CPU Usage

PromQL:

sum(rate(container_cpu_usage_seconds_total{pod=~"${{ values.component_id }}.*"}[5m])) by (pod)

Recommended visualization:

Time series
Panel 8: Memory Usage

PromQL:

container_memory_working_set_bytes{pod=~"${{ values.component_id }}.*"}

Recommended visualization:

Time series
Panel 9: Kubernetes Events

Use Loki or event exporter logs if available.

Example LogQL:

{namespace="dev"} |= "${{ values.component_id }}"
Panel 10: Application Logs

LogQL:

{app="${{ values.component_id }}"}

Useful filters:

{app="${{ values.component_id }}"} |= "error"
{app="${{ values.component_id }}"} |= "database"
{app="${{ values.component_id }}"} |= "timeout"
Dashboard Variables

Recommended variables:

Variable	Example
namespace	dev
service	${{ values.component_id }}
pod	${{ values.component_id }}.*
environment	dev, devops, production
SLO Panels

Include these SLO panels:

Availability SLO
Error budget remaining
Error rate burn
Latency compliance
Deployment health

