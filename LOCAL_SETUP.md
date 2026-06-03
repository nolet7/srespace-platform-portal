# SRESpace Platform Portal - Local Setup

This repository contains the SRESpace Backstage Platform Portal.

It is configured for local development with:

- Backstage frontend and backend
- GitHub OAuth authentication
- GitHub catalog integration
- PostgreSQL persistence
- TechDocs with MkDocs
- Local startup script

---

## 1. Prerequisites

Install these on the laptop:

- Docker Desktop
- Node.js LTS
- Git
- Python 3.11 or newer
- Yarn via Corepack
- VS Code

Verify:

```bash
node -v
yarn -v
git --version
python --version
docker --version
2. Environment file

Copy the sample file:

cp .env.example .env

Update .env with real local values:

GITHUB_CLIENT_ID=your_github_oauth_client_id
GITHUB_CLIENT_SECRET=your_github_oauth_client_secret
GITHUB_TOKEN=your_github_personal_access_token

AUTH_GITHUB_CLIENT_ID=${GITHUB_CLIENT_ID}
AUTH_GITHUB_CLIENT_SECRET=${GITHUB_CLIENT_SECRET}

POSTGRES_HOST=localhost
POSTGRES_PORT=5433
POSTGRES_USER=backstage
POSTGRES_PASSWORD=your_local_postgres_password
POSTGRES_DATABASE=backstage

Do not commit .env.

3. PostgreSQL container

Start local PostgreSQL:

docker run -d \
  --name backstage-postgres \
  -e POSTGRES_USER=backstage \
  -e POSTGRES_PASSWORD=your_local_postgres_password \
  -e POSTGRES_DB=backstage \
  -p 5433:5432 \
  -v backstage-postgres-data:/var/lib/postgresql/data \
  postgres:16

Verify:

docker exec -it backstage-postgres pg_isready -U backstage -d backstage
4. TechDocs Python environment

Create and activate the TechDocs virtual environment:

python -m venv .venv-techdocs
source .venv-techdocs/Scripts/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install mkdocs-techdocs-core
mkdocs --version

Expected:

mkdocs, version 1.6.1
5. Install Backstage dependencies
yarn install
6. Start Backstage

Recommended startup:

./scripts/start-backstage-local.sh

Manual startup:

source .venv-techdocs/Scripts/activate

set -a
source .env
set +a

yarn start

Open the URL printed by Backstage, usually:

http://localhost:3000

or:

http://localhost:3002
7. GitHub OAuth callback

The GitHub OAuth App should use:

Homepage URL:
http://localhost:3000

Authorization callback URL:
http://localhost:7007/api/auth/github/handler/frame

If Backstage runs on another frontend port like 3002, update the OAuth homepage if needed.

8. Important ignored files

These files and folders should not be committed:

.env
node_modules/
.venv-techdocs/
.techdocs/
*.sqlite
dist/
dist-types/

