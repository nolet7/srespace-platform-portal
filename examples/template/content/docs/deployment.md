# Deployment

## Docker

```bash
docker build -t ${{ values.serviceName }}:local .
docker run -p ${{ values.port }}:${{ values.port }} ${{ values.serviceName }}:local
```

## Helm

```bash
helm upgrade --install ${{ values.serviceName }} ./helm -n ${{ values.namespace }} --create-namespace
```

## Kubernetes Namespace

```bash
kubectl create namespace ${{ values.namespace }}
```
