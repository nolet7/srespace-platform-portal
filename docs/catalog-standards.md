# Catalog Standards

Every application repository should include a Backstage catalog file.

Recommended location:

```text
backstage/catalog-info.yaml
```

## Required fields

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: service-name
  namespace: default
  description: Service description
  annotations:
    github.com/project-slug: owner/repository
    backstage.io/techdocs-ref: dir:.
spec:
  type: service
  lifecycle: development
  owner: platform-engineering
```
