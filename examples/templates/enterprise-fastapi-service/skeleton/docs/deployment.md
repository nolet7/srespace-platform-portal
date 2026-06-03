# Deployment

## Docker Build

    docker build -t noletengine/${{ values.name }}:latest .

## Docker Run

    docker run -p 8000:8000 noletengine/${{ values.name }}:latest

## Kubernetes Deploy

    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml

## Validation

    kubectl get pods
    kubectl get svc
    kubectl logs deploy/${{ values.name }}

## Rollback

Check rollout history:

    kubectl rollout history deployment/${{ values.name }}

Rollback to previous version:

    kubectl rollout undo deployment/${{ values.name }}
