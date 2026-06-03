# Observability

## Overview

This service is prepared for Prometheus and Grafana monitoring.

## Metrics Endpoint

The service exposes metrics at:

    /metrics

## Prometheus ServiceMonitor

A ServiceMonitor is included for Prometheus Operator based environments.

Apply manually:

    kubectl apply -f k8s/servicemonitor.yaml -n dev

Or deploy through Helm:

    helm upgrade --install ${{ values.name }} ./helm -n dev --create-namespace

## Prometheus Validation

Check that the ServiceMonitor exists:

    kubectl get servicemonitor -n dev

Check that Prometheus discovered the target:

    kubectl port-forward svc/prometheus-operated -n monitoring 9090:9090

Then open:

    http://localhost:9090/targets

## Suggested Grafana Panels

| Panel | PromQL |
|---|---|
| Request rate | `rate(http_requests_total[5m])` |
| Error rate | `rate(http_requests_total{status=~"5.."}[5m])` |
| p95 latency | `histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))` |
| Pod restarts | `increase(kube_pod_container_status_restarts_total[15m])` |
| CPU usage | `rate(container_cpu_usage_seconds_total[5m])` |
| Memory usage | `container_memory_working_set_bytes` |

## Alert Examples

| Alert | Condition |
|---|---|
| High error rate | Error rate greater than 1% for 10 minutes |
| High latency | p95 latency greater than 300ms for 10 minutes |
| Pod restarts | Restart count increases within 15 minutes |
| Target down | Prometheus target is down for 5 minutes |
