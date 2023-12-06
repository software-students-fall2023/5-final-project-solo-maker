import pytest
from app import app as flask_app  # Import your Flask app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_datasource_post(client):
    # Test POST request with UID
    response = client.post('/api/v1/datasource/', data={'uid': '12345'})
    assert response.status_code == 200
    # Further assertions based on expected behavior


def test_datasource_post_no_uid(client):
    response = client.post('/api/v1/datasource/')
    assert response.status_code == 200
    assert b"No UID provided" in response.data


def test_datasource_get(client):
    response = client.get('/api/v1/datasource/')
    assert response.status_code == 200
    assert b"Invalid request method" in response.data


