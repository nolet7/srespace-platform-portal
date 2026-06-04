# SLO Definition

## Purpose

This document defines the standard Service Level Objectives for applications generated from the Full-Stack PostgreSQL Golden Path template.

## Service Overview

Service name:

```text
${{ values.component_id }}

Owner:

${{ values.owner }}
Recommended SLIs
SLI	Description	Example Measurement
Availability	Percentage of successful requests	HTTP 2xx and 3xx responses
Error Rate	Percentage of failed requests	HTTP 5xx responses
Latency	Request duration	p95 or p99 response time
Saturation	Resource pressure	CPU, memory, connection pool usage
Traffic	Request volume	Requests per second
Database Health	DB availability and query performance	Connection errors and slow queries
Availability SLO

Target:

99.9%

Meaning:

The service should successfully respond to 99.9% of valid requests during the measurement window.

Example PromQL:

(
  sum(rate(http_requests_total{job="${{ values.component_id }}",status!~"5.."}[5m]))
  /
  sum(rate(http_requests_total{job="${{ values.component_id }}"}[5m]))
) * 100
Error Rate SLO

Target:

Less than 1% 5xx errors

Example PromQL:

(
  sum(rate(http_requests_total{job="${{ values.component_id }}",status=~"5.."}[5m]))
  /
  sum(rate(http_requests_total{job="${{ values.component_id }}"}[5m]))
) * 100
Latency SLO

Target:

95% of requests should complete under 300ms

Example PromQL:

histogram_quantile(
  0.95,
  sum(rate(http_request_duration_seconds_bucket{job="${{ values.component_id }}"}[5m])) by (le)
)
Kubernetes Reliability Indicators

Track these Kubernetes indicators:

Indicator	Why It Matters
Pod restarts	Detect crash loops or unstable releases
Ready replicas	Confirm the deployment is serving traffic
CPU usage	Detect saturation or under-provisioning
Memory usage	Detect leaks or memory pressure
Pending pods	Detect scheduling or capacity issues
Failed probes	Detect bad health checks or app startup issues
Error Budget

For a 99.9% monthly availability SLO, the approximate monthly error budget is:

43.2 minutes of allowed downtime per 30-day month
Alerting Recommendations
Alert	Condition	Severity
HighErrorRate	5xx error rate greater than 1% for 5 minutes	warning
CriticalErrorRate	5xx error rate greater than 5% for 5 minutes	critical
HighLatency	p95 latency greater than 300ms for 10 minutes	warning
PodCrashLooping	Pod repeatedly restarts	critical
DeploymentUnavailable	Available replicas less than desired replicas	critical
DatabaseConnectionFailure	API cannot connect to PostgreSQL	critical
SLO Review Process

Review this SLO:

Weekly during active development
Monthly for production services
After every major incident
After every major architecture change
Production Readiness Requirement

Before production, confirm:

SLIs are defined
SLO targets are documented
Prometheus metrics are available
Grafana dashboard exists
Alerts are configured
Runbook exists
Owner is assigned in Backstage
Rollback process is documented

