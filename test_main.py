from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the CI/CD Pipeline API!"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_add_numbers():
    response = client.get("/add?a=5.0&b=10.0")
    assert response.status_code == 200
    assert response.json() == {"result": 15.0}

def test_substract_numbers():
    response = client.post("/subtract", json={"a": 10.0, "b": 5.0})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}
