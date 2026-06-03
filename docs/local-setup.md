# Local Setup

## Start local Backstage

From the portal repository root:

```bash
cd /c/Users/Lateef/Downloads/platform/platform-lesson/platform-eng/backstage-from-wsl
./scripts/start-backstage-local.sh
```

## Required local services

The local setup uses Docker Desktop, PostgreSQL, GitHub OAuth credentials, a GitHub token, a Python virtual environment for TechDocs, and Yarn.

## Environment file

Create a local `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Do not commit `.env`.

## PostgreSQL

Backstage uses local PostgreSQL on:

```text
localhost:5433
```

Container name:

```text
backstage-postgres
```
