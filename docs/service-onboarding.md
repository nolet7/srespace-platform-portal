# Service Onboarding

## Objective

Service onboarding ensures every application has ownership, documentation, operational guidance, and platform visibility before production use.

## Onboarding Workflow

    Developer requests service
      |
      v
    Software template generates repository
      |
      v
    Catalog metadata is created
      |
      v
    TechDocs are created
      |
      v
    CI/CD workflow is enabled
      |
      v
    Service appears in Backstage catalog

## Required Repository Structure

    service-repo/
      backstage/
        catalog-info.yaml
        mkdocs.yml
        docs/
          index.md
          architecture.md
          deployment.md
          runbook.md
          slos.md

## Required Metadata

| Field | Required | Example |
|---|---|---|
| name | Yes | payment-service |
| owner | Yes | platform-engineering |
| lifecycle | Yes | development |
| type | Yes | service |
| github project slug | Yes | nolet7/python-app |
| techdocs ref | Yes | dir:. |

## Acceptance Criteria

A service is considered onboarded when:

- It appears in the Backstage catalog
- Ownership is assigned
- TechDocs render successfully
- Runbook exists
- Deployment path is documented
- Monitoring expectations are documented
- Repository link is available
