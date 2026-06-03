# Observability and SLOs

## Objective

The portal helps teams understand reliability expectations, dashboard ownership, alerting standards, and service-level targets.

## Recommended SLIs

| SLI | Description |
|---|---|
| Availability | Percentage of successful requests |
| Latency | p95 or p99 response time |
| Error rate | Percentage of failed requests |
| Saturation | CPU, memory, queue depth, connection usage |
| Freshness | Data or documentation update age |

## Example SLOs

| Service Type | Example SLO |
|---|---|
| User-facing API | 99.9% availability monthly |
| Internal service | 99.5% availability monthly |
| Batch job | 99% completion success |
| TechDocs generation | Successful generation on main branch |

## Alerting Principles

- Alert on user impact, not noise
- Use burn-rate style alerts for SLOs
- Link alerts to runbooks
- Include ownership metadata
- Include dashboard links
- Include escalation path

## Service Documentation Standard

Every critical service should document:

- SLIs
- SLO targets
- Error budget policy
- Dashboard links
- Alert names
- Runbook links
- Escalation contacts
