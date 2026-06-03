
Deployment
Docker Build
docker build -t ${{ values.dockerImage }} .
Kubernetes Deploy
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
Validation
kubectl get pods
kubectl get svc
kubectl logs deploy/${{ values.name }}
Rollback

Use Kubernetes rollout history:

kubectl rollout history deployment/${{ values.name }}
kubectl rollout undo deployment/${{ values.name }}

