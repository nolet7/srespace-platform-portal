# Reliability Controls

## Overview

This service includes production reliability controls for Kubernetes-based environments.

## Included Controls

| Control | Purpose |
|---|---|
| HorizontalPodAutoscaler | Scales pods based on CPU utilization |
| PodDisruptionBudget | Keeps at least one pod available during voluntary disruptions |
| NetworkPolicy | Limits inbound access to the application pods |
| Readiness Probe | Prevents traffic from reaching unready pods |
| Liveness Probe | Restarts unhealthy containers |
| Resource Requests and Limits | Protects cluster capacity and workload stability |

## Apply Reliability Manifests

Apply with raw Kubernetes manifests:

    kubectl apply -f k8s/deployment.yaml -n dev
    kubectl apply -f k8s/service.yaml -n dev
    kubectl apply -f k8s/hpa.yaml -n dev
    kubectl apply -f k8s/pdb.yaml -n dev
    kubectl apply -f k8s/networkpolicy.yaml -n dev

Or deploy with Helm:

    helm upgrade --install ${{ values.name }} ./helm -n dev --create-namespace

## Validate

Check pods:

    kubectl get pods -n dev -l app=${{ values.name }}

Check autoscaling:

    kubectl get hpa -n dev

Check disruption budget:

    kubectl get pdb -n dev

Check network policy:

    kubectl get networkpolicy -n dev

## Operational Notes

If the service becomes unreachable after applying NetworkPolicy, verify that your ingress controller, Prometheus, or gateway namespace is allowed to connect to the pod.

If HPA does not show CPU metrics, verify that Metrics Server is installed in the cluster.
