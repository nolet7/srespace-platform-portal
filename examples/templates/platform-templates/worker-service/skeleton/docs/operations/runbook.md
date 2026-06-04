# Operations Runbook

## Common Commands

kubectl get pods -n dev

kubectl get svc -n dev

kubectl get ingress -n dev

## Troubleshooting

Check logs:

kubectl logs -n dev deploy/${{ values.component_id }} --tail=100

Restart deployment:

kubectl rollout restart deploy/${{ values.component_id }} -n dev
