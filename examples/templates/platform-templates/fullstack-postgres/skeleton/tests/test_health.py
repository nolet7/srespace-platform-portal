from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert "service" in data
    assert "environment" in data


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert "service" in data
    assert "health" in data
    assert "metrics" in data


def test_categories_endpoint():
    response = client.get("/api/categories")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_products_endpoint():
    response = client.get("/api/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_metrics_endpoint():
    response = client.get("/metrics")

    assert response.status_code == 200
    assert "http_requests_total" in response.text
