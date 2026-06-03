# Operating Model

## Team Model

The portal is operated by the Platform Engineering team and consumed by application, SRE, DevOps, and operations teams.

| Team | Responsibility |
|---|---|
| Platform Engineering | Portal ownership, templates, catalog standards |
| SRE | Runbooks, SLOs, reliability standards |
| Application Teams | Service metadata, service docs, ownership accuracy |
| Security | Access standards, secret handling, policy guidance |
| Engineering Leadership | Roadmap, adoption metrics, governance |

## RACI

| Activity | Platform | SRE | App Team | Security |
|---|---|---|---|---|
| Maintain portal | A/R | C | I | C |
| Register services | C | C | A/R | I |
| Maintain runbooks | C | A/R | R | I |
| Maintain templates | A/R | C | C | C |
| Review access patterns | C | I | I | A/R |
| Define SLO standards | C | A/R | C | I |

## Lifecycle States

| Lifecycle | Meaning |
|---|---|
| experimental | Early proof of concept |
| development | Actively being built |
| production | Production service |
| deprecated | Scheduled for retirement |

## Minimum Service Standard

A production-ready catalog entity should have:

- Owner
- Repository link
- Lifecycle
- System association
- TechDocs
- Runbook
- Deployment documentation
- SLO or service-level target
- Escalation path
