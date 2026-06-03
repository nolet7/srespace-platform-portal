# Troubleshooting

## Pod CrashLoopBackOff

Check logs:

    kubectl logs deploy/${{ values.name }}

Describe the pod:

    kubectl describe pod -l app=${{ values.name }}

## Readiness Probe Failing

Check the readiness endpoint:

    curl http://localhost:8000/ready

Expected response:

    {"status":"ready"}

## Liveness Probe Failing

Check the health endpoint:

    curl http://localhost:8000/health

Expected response:

    {"status":"healthy"}

## Metrics Not Scraped

Confirm the metrics endpoint is reachable:

    curl http://localhost:8000/metrics

Then verify Prometheus scrape configuration or ServiceMonitor configuration.
