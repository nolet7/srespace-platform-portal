# Architecture

## Logical Architecture

    Users
      |
      v
    Backstage Frontend
      |
      v
    Backstage Backend
      |
      +--> PostgreSQL
      +--> GitHub OAuth
      +--> GitHub Catalog Provider
      +--> TechDocs Generator
      +--> Software Templates
      +--> Kubernetes Plugin

## Component Responsibilities

| Component | Responsibility |
|---|---|
| Backstage frontend | Developer portal UI |
| Backstage backend | API, authentication, catalog, plugins |
| PostgreSQL | Persistent application data |
| GitHub OAuth | User login and identity mapping |
| GitHub token | Repository and catalog access |
| TechDocs | Documentation generation and rendering |
| Catalog | Service metadata and ownership |
| Software templates | Standardized service scaffolding |

## Repository Separation

    srespace-platform-portal
      Full Backstage portal application and platform documentation

    python-app
      Example application, catalog metadata, and service TechDocs

## Catalog Flow

    GitHub repository
      |
      +--> backstage/catalog-info.yaml
              |
              v
    Backstage catalog processor
              |
              v
    Service entity visible in portal

## TechDocs Flow

    Repository docs + mkdocs.yml
      |
      v
    TechDocs generator
      |
      v
    Generated static documentation
      |
      v
    Backstage Docs UI

## Enterprise Design Principles

- Source of truth lives in Git
- Documentation is versioned with code
- Every service has an owner
- Every service has a lifecycle
- Operational procedures are discoverable
- Platform patterns are reusable
- Security and governance are built into templates
