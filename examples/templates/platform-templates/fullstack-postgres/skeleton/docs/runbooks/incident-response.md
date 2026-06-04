# Incident Response Runbook

## Purpose

This runbook provides a standard incident response process for applications generated from the Full-Stack PostgreSQL Golden Path template.

## Service Information

Service:

```text
${{ values.component_id }}
Owner:

${{ values.owner }}
Incident Severity Levels
Severity	Description	Example
SEV1	Full outage or major customer impact	API unavailable
SEV2	Partial outage or serious degradation	High error rate
SEV3	Minor degradation	Elevated latency
SEV4	Informational issue	Non-critical warning
Step 1: Confirm the Alert

Check the alert source:

argocd app get ${{ values.component_id }}
kubectl get pods -n dev | grep ${{ values.component_id }}
kubectl get ingress -n dev

Check application health:

curl -s http://${{ values.component_id }}.localhost/api/health
Step 2: Check Recent Deployments
kubectl rollout history deploy/${{ values.component_id }}-api -n dev
kubectl rollout history deploy/${{ values.component_id }} -n dev
argocd app history ${{ values.component_id }}
Step 3: Check Pods
kubectl get pods -n dev | grep ${{ values.component_id }}
kubectl describe pod -n dev <pod-name>

Look for:

CrashLoopBackOff
ImagePullBackOff
Pending pods
Failed readiness probes
Failed liveness probes
OOMKilled containers
Scheduling failures
Step 4: Check Logs

API logs:

kubectl logs -n dev deploy/${{ values.component_id }}-api --tail=200

Frontend logs:

kubectl logs -n dev deploy/${{ values.component_id }} --tail=200

PostgreSQL logs:

kubectl logs -n dev deploy/${{ values.component_id }}-postgres --tail=200
Step 5: Check Services and Endpoints
kubectl get svc -n dev | grep ${{ values.component_id }}
kubectl get endpoints -n dev | grep ${{ values.component_id }}

If a service has no endpoints, check:

Pod labels
Service selectors
Readiness probe failures
Deployment status
Step 6: Check Kubernetes Events
kubectl get events -n dev --sort-by=.lastTimestamp

Look for:

Failed scheduling
Failed image pull
Failed mount
Probe failures
Resource pressure
Step 7: Check Resource Usage
kubectl top pods -n dev
kubectl top nodes

Look for:

High CPU
High memory
Node pressure
OOMKilled containers
Step 8: Check Database Connectivity
kubectl get pods -n dev | grep postgres
kubectl get svc -n dev | grep postgres
kubectl logs -n dev deploy/${{ values.component_id }}-postgres --tail=100

Common database issues:

Wrong database hostname
Wrong username or password
Missing secret
PostgreSQL pod not ready
PVC issue
NetworkPolicy blocking access
Step 9: Roll Back If Needed

If the incident started after a deployment, roll back.

Kubernetes rollback:

kubectl rollout undo deploy/${{ values.component_id }}-api -n dev
kubectl rollout status deploy/${{ values.component_id }}-api -n dev

Argo CD rollback:

argocd app history ${{ values.component_id }}
argocd app rollback ${{ values.component_id }} <revision-id>
Step 10: Communicate Status

Recommended update format:

Incident:
Impact:
Current status:
Action being taken:
Next update:
Owner:
Step 11: Resolve and Verify

After fixing the issue, verify:

kubectl get pods -n dev | grep ${{ values.component_id }}
curl -s http://${{ values.component_id }}.localhost/api/health
argocd app get ${{ values.component_id }}

Confirm:

Pods are Running
Readiness is healthy
Health endpoint works
Error rate is normal
Latency is normal
Argo CD is Synced and Healthy
Step 12: Post-Incident Review

Document:

What happened
Customer or user impact
Timeline
Root cause
What fixed the issue
What can prevent recurrence
Follow-up tasks
Owner for each task
Common Incident Fixes
Issue	Quick Check	Common Fix
CrashLoopBackOff	kubectl logs	Fix app config or secret
ImagePullBackOff	kubectl describe pod	Fix image name or registry credentials
Pending pod	kubectl describe pod	Add resources or fix PVC
503 ingress error	kubectl get endpoints	Fix service selector or readiness
API down	Health endpoint and logs	Restart or roll back API
DB connection failure	API and DB logs	Fix secret or service name
Argo CD OutOfSync	argocd app diff	Sync app or fix Git manifest

