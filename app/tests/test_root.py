import pytest
from fastapi import status
from fastapi.testclient import TestClient
from httpx import AsyncClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root(client: AsyncClient) -> None:
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World"}
