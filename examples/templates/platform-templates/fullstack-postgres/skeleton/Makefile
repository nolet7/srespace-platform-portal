.RECIPEPREFIX := >

APP_NAME=${{ values.component_id }}
NAMESPACE=dev
FRONTEND_IMAGE=noletengine/${{ values.component_id }}:latest
BACKEND_IMAGE=noletengine/${{ values.component_id }}-api:latest

.PHONY: help install-backend test-backend run-backend docker-build docker-up docker-down helm-lint helm-template helm-install helm-upgrade helm-uninstall argocd-apply k8s-status clean

help:
> echo "Available commands:"
> echo "  make install-backend   Install backend dependencies"
> echo "  make test-backend      Run backend tests"
> echo "  make run-backend       Run backend locally"
> echo "  make docker-build      Build frontend and backend Docker images"
> echo "  make docker-up         Start app locally with Docker Compose"
> echo "  make docker-down       Stop Docker Compose"
> echo "  make helm-lint         Validate Helm chart"
> echo "  make helm-template     Render Helm manifests"
> echo "  make helm-install      Install app with Helm"
> echo "  make helm-upgrade      Upgrade app with Helm"
> echo "  make helm-uninstall    Remove app with Helm"
> echo "  make argocd-apply      Apply Argo CD Application manifest"
> echo "  make k8s-status        Show Kubernetes app status"
> echo "  make clean             Clean local temporary files"

install-backend:
> cd backend && python -m pip install --upgrade pip
> cd backend && pip install -r requirements.txt

test-backend:
> pytest -q

run-backend:
> cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

docker-build:
> docker build -t $(FRONTEND_IMAGE) .
> docker build -t $(BACKEND_IMAGE) backend

docker-up:
> docker compose up -d --build

docker-down:
> docker compose down

helm-lint:
> helm lint helm

helm-template:
> helm template $(APP_NAME) helm --namespace $(NAMESPACE)

helm-install:
> helm upgrade --install $(APP_NAME) ./helm -n $(NAMESPACE) --create-namespace

helm-upgrade:
> helm upgrade $(APP_NAME) ./helm -n $(NAMESPACE)

helm-uninstall:
> helm uninstall $(APP_NAME) -n $(NAMESPACE)

argocd-apply:
> kubectl apply -f argocd/application.yaml

k8s-status:
> kubectl get pods -n $(NAMESPACE) | grep $(APP_NAME) || true
> kubectl get svc -n $(NAMESPACE) | grep $(APP_NAME) || true
> kubectl get ingress -n $(NAMESPACE) || true

clean:
> find . -type d -name "__pycache__" -prune -exec rm -rf {} +
> find . -type d -name ".pytest_cache" -prune -exec rm -rf {} +
> find . -type f -name "*.pyc" -delete
