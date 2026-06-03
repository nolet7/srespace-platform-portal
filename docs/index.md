# SRESpace Platform Portal

The **SRESpace Platform Portal** is an enterprise-style Backstage developer portal for SRE, Platform Engineering, DevOps, and application teams.

It provides one governed place to discover services, document ownership, generate new application scaffolds, publish operational runbooks, and standardize platform engineering practices across repositories.

## Business Purpose

The portal helps reduce manual platform tickets by making common engineering requests self-service and auditable.

| Capability | Business Value |
|---|---|
| Service catalog | Central ownership and system visibility |
| TechDocs | Consistent documentation and runbooks |
| Software templates | Faster service onboarding with standard controls |
| GitHub integration | Repository discovery and catalog automation |
| Kubernetes visibility | Platform-level workload awareness |
| SRE documentation | Faster incident response and operational readiness |

## Current Scope

| Area | Status |
|---|---|
| Backstage application | Running locally |
| GitHub OAuth | Enabled |
| PostgreSQL persistence | Enabled locally |
| TechDocs | Enabled with MkDocs |
| Catalog registration | Enabled |
| Example service | `python-app` |
| Platform portal entity | `backstage-portal` |

## Key Repositories

| Repository | Purpose |
|---|---|
| `nolet7/srespace-platform-portal` | Full Backstage portal application |
| `nolet7/python-app` | Example application with catalog metadata and TechDocs |

## Enterprise Outcomes

This portal is designed to support faster onboarding, clear ownership, standardized documentation, repeatable deployment patterns, better incident response, improved audit readiness, and reduced operational toil.
