# Architecture

## Local Architecture

```text
Browser
  |
  v
Backstage Frontend
  |
  v
Backstage Backend
  |
  +--> PostgreSQL
  +--> GitHub API
  +--> TechDocs Generator
  +--> Catalog Processor
```

## Repository Separation

```text
srespace-platform-portal = full Backstage portal application
python-app                = application code, catalog-info.yaml, and TechDocs
```
