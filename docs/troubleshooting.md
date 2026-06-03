# Troubleshooting

## GitHub sign-in fails

Load the environment variables:

```bash
set -a
source .env
set +a
```

Verify variables are set without printing secrets:

```bash
[ -n "$AUTH_GITHUB_CLIENT_ID" ] && echo "AUTH_GITHUB_CLIENT_ID is set"
[ -n "$AUTH_GITHUB_CLIENT_SECRET" ] && echo "AUTH_GITHUB_CLIENT_SECRET is set"
[ -n "$GITHUB_TOKEN" ] && echo "GITHUB_TOKEN is set"
```

## TechDocs error: spawn mkdocs ENOENT

Activate the TechDocs Python environment:

```bash
source .venv-techdocs/Scripts/activate
mkdocs --version
```

## PostgreSQL not running

```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
docker start backstage-postgres
```
