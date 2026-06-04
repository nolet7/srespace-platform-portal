# Rollback Runbook

## Purpose

This runbook explains how to roll back an application generated from the Full-Stack PostgreSQL Golden Path template.

Use this when a new deployment causes:

- API failures
- Frontend failures
- High error rate
- High latency
- Database connection issues
- Failed readiness or liveness probes
- Argo CD sync problems

## Service Information

Service:

```text
${{ values.component_id }}

Owner:

${{ values.owner }}
Step 1: Confirm Current Application State
kubectl get pods -n dev | grep ${{ values.component_id }}
kubectl get svc -n dev | grep ${{ values.component_id }}
kubectl get ingress -n dev
argocd app get ${{ values.component_id }}
Step 2: Check Rollout History

API deployment:

kubectl rollout history deploy/${{ values.component_id }}-api -n dev

Frontend deployment:

kubectl rollout history deploy/${{ values.component_id }} -n dev

Argo CD history:

argocd app history ${{ values.component_id }}
Step 3: Roll Back API Deployment
kubectl rollout undo deploy/${{ values.component_id }}-api -n dev
kubectl rollout status deploy/${{ values.component_id }}-api -n dev
Step 4: Roll Back Frontend Deployment
kubectl rollout undo deploy/${{ values.component_id }} -n dev
kubectl rollout status deploy/${{ values.component_id }} -n dev
Step 5: Roll Back to a Specific Kubernetes Revision

First list rollout history:

kubectl rollout history deploy/${{ values.component_id }}-api -n dev

Then roll back to a specific revision:

kubectl rollout undo deploy/${{ values.component_id }}-api -n dev --to-revision=<revision-number>
Step 6: Roll Back with Argo CD

List Argo CD application history:

argocd app history ${{ values.component_id }}

Roll back to a specific revision:

argocd app rollback ${{ values.component_id }} <revision-id>

Then verify:

argocd app get ${{ values.component_id }}
Step 7: Verify Pods After Rollback
kubectl get pods -n dev | grep ${{ values.component_id }}
kubectl get events -n dev --sort-by=.lastTimestamp

Expected result:

Pods should be Running and Ready.
Step 8: Verify Application Health
curl -s http://${{ values.component_id }}.localhost/api/health

Expected result:

{
  "status": "healthy"
}
Step 9: Verify Logs

API logs:

kubectl logs -n dev deploy/${{ values.component_id }}-api --tail=100

Frontend logs:

kubectl logs -n dev deploy/${{ values.component_id }} --tail=100
Step 10: Verify Metrics

Check Grafana and Prometheus for:

Error rate returning to normal
Latency returning to normal
Pod restarts stopping
Availability recovering
Database errors stopping
Step 11: Document the Rollback

Record:

Service:
Environment:
Deployment version before rollback:
Deployment version after rollback:
Reason for rollback:
Impact:
Rollback command used:
Validation result:
Owner:
Follow-up action:
Common Rollback Scenarios
Scenario	Recommended Action
New API version fails	Roll back API deployment
New frontend fails	Roll back frontend deployment
Bad Helm values	Revert Git commit and sync Argo CD
Bad image tag	Revert image tag and sync Argo CD
Database migration issue	Stop rollout and follow DB recovery plan
Argo CD out of sync	Compare app diff and sync known-good revision
Emergency Commands

Restart API:

kubectl rollout restart deploy/${{ values.component_id }}-api -n dev

Restart frontend:

kubectl rollout restart deploy/${{ values.component_id }} -n dev

Force Argo CD sync:

argocd app sync ${{ values.component_id }}

Check Argo CD diff:

argocd app diff ${{ values.component_id }}

