
Runbook
Service Down
Check pod status.
Check service endpoints.
Review logs.
Validate image tag.
Confirm readiness and liveness probes.
Commands
kubectl get pods -l app=${{ values.name }}
kubectl describe deploy ${{ values.name }}
kubectl logs deploy/${{ values.name }}
Escalation

Escalate to ${{ values.owner }} when service health cannot be restored.
