# Operations Runbook

## Purpose

This runbook provides standard operational commands for applications generated from the Full-Stack PostgreSQL Golden Path template.

## 1. Check Namespace

```bash
kubectl get ns
kubectl get ns dev
````

## 2. Check Application Pods

```bash
kubectl get pods -n dev
kubectl get pods -n dev | grep ${{ values.component_id }}
```

Expected result:

```text
Pods should be Running and Ready.
```

## 3. Check Services

```bash
kubectl get svc -n dev
kubectl get svc -n dev | grep ${{ values.component_id }}
```

## 4. Check Ingress

```bash
kubectl get ingress -n dev
kubectl describe ingress -n dev
```

## 5. Check Application Health

```bash
curl -s http://${{ values.component_id }}.localhost/api/health
```

Expected result:

```json
{
  "status": "healthy"
}
```

## 6. Check API Logs

```bash
kubectl logs -n dev deploy/${{ values.component_id }}-api --tail=100
```

## 7. Check Frontend Logs

```bash
kubectl logs -n dev deploy/${{ values.component_id }} --tail=100
```

## 8. Check PostgreSQL Pod

```bash
kubectl get pods -n dev | grep postgres
kubectl logs -n dev deploy/${{ values.component_id }}-postgres --tail=100
```

## 9. Restart API Deployment

```bash
kubectl rollout restart deploy/${{ values.component_id }}-api -n dev
kubectl rollout status deploy/${{ values.component_id }}-api -n dev
```

## 10. Restart Frontend Deployment

```bash
kubectl rollout restart deploy/${{ values.component_id }} -n dev
kubectl rollout status deploy/${{ values.component_id }} -n dev
```

## 11. Describe Failing Pod

```bash
kubectl describe pod -n dev <pod-name>
```

## 12. Check Recent Events

```bash
kubectl get events -n dev --sort-by=.lastTimestamp
```

## 13. Check Resource Usage

```bash
kubectl top pods -n dev
kubectl top nodes
```

## 14. Port Forward API for Local Debugging

```bash
kubectl port-forward -n dev svc/${{ values.component_id }}-api 8000:8000
```

Then test:

```bash
curl -s http://localhost:8000/api/health
```

## 15. Roll Back Deployment

```bash
kubectl rollout history deploy/${{ values.component_id }}-api -n dev
kubectl rollout undo deploy/${{ values.component_id }}-api -n dev
kubectl rollout status deploy/${{ values.component_id }}-api -n dev
```

## 16. Argo CD Sync Check

```bash
argocd app get ${{ values.component_id }}
argocd app sync ${{ values.component_id }}
```

## Common Issues

| Issue                 | Check                       | Fix                                      |
| --------------------- | --------------------------- | ---------------------------------------- |
| Pod stuck in Pending  | `kubectl describe pod`      | Check CPU/memory or PVC                  |
| CrashLoopBackOff      | `kubectl logs`              | Fix app config or secret                 |
| ImagePullBackOff      | `kubectl describe pod`      | Check image name and registry auth       |
| 503 from ingress      | `kubectl get endpoints`     | Check service selector and pod readiness |
| API not reachable     | `kubectl get svc,endpoints` | Validate service targetPort              |
| DB connection failure | API logs and secrets        | Validate DB host, user, password         |
| Argo CD OutOfSync     | `argocd app diff`           | Sync or fix Git manifest                 |

