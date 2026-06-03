# CI/CD and GitOps

## Objective

Standardize how code moves from repository to runtime using repeatable automation.

## Recommended Pipeline Stages

    Commit
      |
      v
    Build
      |
      v
    Unit tests
      |
      v
    Security scans
      |
      v
    Container image build
      |
      v
    Push image
      |
      v
    Deploy through Helm or GitOps
      |
      v
    Verify health and rollback evidence

## GitOps Pattern

| Component | Purpose |
|---|---|
| GitHub | Source control |
| GitHub Actions | Build and validation pipeline |
| Docker registry | Image storage |
| Helm | Deployment packaging |
| Argo CD | Continuous delivery and drift correction |

## Required Controls

- Pull request review
- Branch protection
- Automated tests
- Secret scanning
- Image tagging strategy
- Rollback procedure
- Environment promotion process
- Deployment evidence

## Recommended Evidence

Each production change should capture:

- Commit SHA
- Image tag
- Pipeline run link
- Deployment time
- Rollback method
- Health check result
