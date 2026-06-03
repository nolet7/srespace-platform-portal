# Disaster Recovery

## Objective

Define how to recover the portal and its supporting services after data loss, workstation failure, configuration corruption, or database failure.

## Protected Assets

| Asset | Recovery Source |
|---|---|
| Backstage source code | GitHub repository |
| TechDocs source | GitHub repository |
| Local PostgreSQL data | Docker volume backup or SQL dump |
| Environment variables | Secure local backup or secrets manager |
| GitHub OAuth app | GitHub developer settings |
| Catalog metadata | Git repository |

## Recovery Strategy

Because the portal is Git-based, most application code and documentation can be restored by cloning the repository.

```bash
git clone https://github.com/nolet7/srespace-platform-portal.git
PostgreSQL Backup Example
docker exec backstage-postgres pg_dump -U backstage backstage > backstage-backup.sql
PostgreSQL Restore Example
cat backstage-backup.sql | docker exec -i backstage-postgres psql -U backstage -d backstage
Recovery Runbook
Install Git, Node.js, Yarn, Python, Docker Desktop, and Git Bash.
Clone the portal repository.
Restore .env from a secure location.
Start PostgreSQL.
Restore database backup if required.
Install dependencies.
Activate the TechDocs Python environment.
Start Backstage.
Validate catalog, sign-in, and TechDocs.
Recovery Validation

After recovery, confirm:

Backstage starts successfully
GitHub sign-in works
backstage-portal appears in the catalog
python-app appears in the catalog
TechDocs pages render successfully
PostgreSQL container is healthy
