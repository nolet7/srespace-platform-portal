# Deployment

## Docker Build

    docker build -t ${{ values.dockerImage }} .

## Docker Run

    docker run -p ${{ values.servicePort }}:${{ values.servicePort }} ${{ values.dockerImage }}

## Kubernetes Deploy

    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml

## Helm Deploy

Install or upgrade the service using Helm:

    helm upgrade --install ${{ values.name }} ./helm -n dev --create-namespace

Validate the release:

    helm list -n dev
    kubectl get pods -n dev
    kubectl get svc -n dev

## Argo CD GitOps Deploy

Apply the generated Argo CD Application:

    kubectl apply -f argocd/application-dev.yaml

Check sync status:

    argocd app get ${{ values.name }}-dev

## Validation

    kubectl get pods -n dev
    kubectl get svc -n dev
    kubectl logs deploy/${{ values.name }} -n dev

## Rollback

Using Kubernetes:

    kubectl rollout history deployment/${{ values.name }} -n dev
    kubectl rollout undo deployment/${{ values.name }} -n dev

Using Helm:

    helm history ${{ values.name }} -n dev
    helm rollback ${{ values.name }} 1 -n dev
