# SLOs

## Recommended SLIs

| SLI | Target |
|---|---|
| Availability | 99.9% |
| p95 latency | < 300 ms |
| Error rate | < 1% |

## Prometheus Metrics

The service exposes metrics at:

```text
/metrics
```

Recommended dashboards:

- Request rate
- Error rate
- p95 latency
- CPU usage
- Memory usage
- Restart count
