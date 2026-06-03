# SLOs

## Reliability Targets

| SLI | Target |
|---|---|
| Availability | 99.9% |
| p95 latency | Less than 300ms |
| Error rate | Less than 1% |
| Readiness success | 99.9% |

## Metrics Endpoint

The service exposes Prometheus-compatible metrics at:

    /metrics

## Error Budget Policy

If the service burns through its error budget:

1. Pause non-critical releases.
2. Review recent deployments.
3. Check application and infrastructure alerts.
4. Prioritize reliability fixes before feature work.
