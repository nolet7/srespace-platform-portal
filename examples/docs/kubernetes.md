
Kubernetes Integration

Backstage can show Kubernetes resources when a component has Kubernetes annotations.

Example:

metadata:
  annotations:
    backstage.io/kubernetes-id: my-service

The Kubernetes plugin can then map catalog entities to workloads running in the cluster.
