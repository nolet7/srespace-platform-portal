# Runbook

## Health Check

```bash
curl http://localhost:${{ values.port }}/healthz
```

## Readiness Check

```bash
curl http://localhost:${{ values.port }}/readyz
```

## Metrics

```bash
curl http://localhost:${{ values.port }}/metrics
```

## Common Issues

- Container image not found
- Pod crash loop
- Missing environment variables
- Service port mismatch
- Ingress routing issue

## Escalation

Owner: ${{ values.owner }}
