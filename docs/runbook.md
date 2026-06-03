# Runbook

## Start Backstage

```bash
cd /c/Users/Lateef/Downloads/platform/platform-lesson/platform-eng/backstage-from-wsl
./scripts/start-backstage-local.sh
```

## Stop Node processes

```bash
taskkill //F //IM node.exe
```

## Check ports

```bash
netstat -ano | grep ":3000\|:3001\|:3002\|:7007"
```

## Start PostgreSQL

```bash
docker start backstage-postgres
```

## Verify PostgreSQL

```bash
docker exec -it backstage-postgres pg_isready -U backstage -d backstage
```

## Clear generated TechDocs cache

```bash
rm -rf .techdocs/default/component/python-app
rm -rf .techdocs/default/component/backstage-portal
```
