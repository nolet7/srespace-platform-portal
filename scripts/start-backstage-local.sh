#!/usr/bin/env bash
set -e

echo "Starting SRESpace Backstage locally..."

cd "$(dirname "$0")/.."

echo "Activating TechDocs Python environment..."
source .venv-techdocs/Scripts/activate

echo "Loading Backstage environment variables..."
set -a
source .env
set +a

echo "Checking PostgreSQL container..."
docker ps --format '{{.Names}}' | grep -q '^backstage-postgres$' || {
  echo "Starting backstage-postgres..."
  docker start backstage-postgres >/dev/null 2>&1 || {
    docker run -d \
      --name backstage-postgres \
      -e POSTGRES_USER="$POSTGRES_USER" \
      -e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" \
      -e POSTGRES_DB="$POSTGRES_DATABASE" \
      -p 5433:5432 \
      -v backstage-postgres-data:/var/lib/postgresql/data \
      postgres:16
  }
}

echo "Checking MkDocs..."
mkdocs --version

echo "Starting Backstage..."
yarn start
