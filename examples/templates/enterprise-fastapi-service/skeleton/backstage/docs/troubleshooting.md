
Troubleshooting
Pod CrashLoopBackOff
kubectl logs deploy/${{ values.name }}
kubectl describe pod -l app=${{ values.name }}
Readiness Probe Failing
curl http://localhost:${{ values.servicePort }}/ready
Metrics Not Scraped

Confirm /metrics is reachable and Prometheus is configured to scrape the service.
EO
F
