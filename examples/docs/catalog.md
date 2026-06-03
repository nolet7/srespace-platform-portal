# Software Catalog

The catalog tracks services, websites, APIs, systems, resources, users, and groups.

## Required Component Fields

Each service should define:

- `metadata.name`
- `metadata.description`
- `metadata.annotations`
- `spec.type`
- `spec.lifecycle`
- `spec.owner`

## Example Owner

Use:

```yaml
spec:
  owner: platform-engineering
