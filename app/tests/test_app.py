import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to CI/CD Flask App" in response.data

def test_status_page(client):
    response = client.get("/status")
    assert response.status_code == 200
    assert response.get_json() == {"status": "success"}