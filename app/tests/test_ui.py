# This test ensures the UI script interacts correctly with the backend
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_ui(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Check Status" in response.data