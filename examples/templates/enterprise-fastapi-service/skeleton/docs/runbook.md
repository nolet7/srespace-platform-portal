# Runbook

## Service Down

Follow this sequence:

1. Check pod status.
2. Check deployment events.
3. Review application logs.
4. Validate image tag.
5. Confirm readiness and liveness probes.
6. Roll back if the latest deployment is unhealthy.

## Commands

Check pods:

    kubectl get pods -l app=${{ values.name }}

Describe deployment:

    kubectl describe deploy ${{ values.name }}

Check logs:

    kubectl logs deploy/${{ values.name }}

## Escalation

Escalate to `${{ values.owner }}` if service health cannot be restored within the expected recovery window.
