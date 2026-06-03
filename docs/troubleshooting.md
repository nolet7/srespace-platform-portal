# Troubleshooting

## GitHub Sign-In Fails

Load environment variables:

    set -a
    source .env
    set +a

Verify variables are set without printing secrets:

    [ -n "$AUTH_GITHUB_CLIENT_ID" ] && echo "AUTH_GITHUB_CLIENT_ID is set"
    [ -n "$AUTH_GITHUB_CLIENT_SECRET" ] && echo "AUTH_GITHUB_CLIENT_SECRET is set"
    [ -n "$GITHUB_TOKEN" ] && echo "GITHUB_TOKEN is set"

## Unable to Resolve User Identity

Confirm the user entity exists and matches the GitHub username resolver.

    cat catalog-user-nolet7.yaml

## TechDocs Error: spawn mkdocs ENOENT

Activate the Python environment:

    source .venv-techdocs/Scripts/activate
    mkdocs --version

If MkDocs is missing:

    python -m venv .venv-techdocs
    source .venv-techdocs/Scripts/activate
    python -m pip install --upgrade pip setuptools wheel
    python -m pip install mkdocs-techdocs-core

## Docs Show Old Content

Clear generated docs and restart Backstage:

    rm -rf .techdocs
    taskkill //F //IM node.exe 2>/dev/null || true
    ./scripts/start-backstage-local.sh

## PostgreSQL Is Unavailable

    docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    docker start backstage-postgres
    docker exec -it backstage-postgres pg_isready -U backstage -d backstage

## Port Already in Use

    netstat -ano | grep ":3000\|:3001\|:3002\|:7007"
    taskkill //F //IM node.exe

## Catalog Entity Missing

Check catalog definitions:

    grep -R -n "name: backstage-portal\|name: python-app" catalog-info.yaml examples/entities.yaml app-config.local.yaml

## Build TechDocs Locally

    source .venv-techdocs/Scripts/activate
    mkdocs build --strict --site-dir /tmp/srespace-platform-portal-techdocs-site
