import pytest
from flask import url_for
from src import create_app
from src.models import mongo, get_notes, save_note, delete_note_by_id
from config import TestingConfig


@pytest.fixture
def app():
    app = create_app(TestingConfig)  # Use TestingConfig
    mongo.init_app(app)

    with app.app_context():
        # Initialize database, if necessary
        pass

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200


def test_add_note_routes(client, mocker):
    mock_save_note = mocker.patch('src.views.save_note')
    get_response = client.get("/add-note")
    assert get_response.status_code == 200
    post_response = client.post("/add-note", data={'title': 'Test', 'description': 'Test Desc'})
    assert post_response.status_code == 302
    mock_save_note.assert_called_once_with('Test', 'Test Desc', mocker.ANY)


def test_get_edit_note_route(client, mocker):
    # Mock get_note_by_id to return a fake note
    fake_note_id = "123"
    fake_note = {'_id': fake_note_id, 'title': 'Test Note', 'description': 'Test Description'}
    mocker.patch('src.views.get_note_by_id', return_value=fake_note)

    # Perform a GET request to the edit-note route
    response = client.get(f'/edit-note?form={fake_note_id}')

    # Check that the status code is 200 (OK)
    assert response.status_code == 200

    # Check that the response contains the note's title and description
    assert b'Test Note' in response.data
    assert b'Test Description' in response.data


def test_post_edit_note_route(client, mocker):
    # Mock update_note_by_id
    mock_update_note_by_id = mocker.patch('src.views.update_note_by_id')

    # Perform a POST request to the edit-note route
    response = client.post('/edit-note', data={'_id': '123', 'title': 'Test Note', 'description': 'Test Description'})

    # Check that the status code is 302 (redirect)
    assert response.status_code == 302

    # Check that update_note_by_id was called with the correct arguments
    mock_update_note_by_id.assert_called_once_with('123', 'Test Note', 'Test Description')


def test_post_delete_note_route(client, mocker):
    # Mock the delete_note_by_id function
    mock_delete_note_by_id = mocker.patch('src.views.delete_note_by_id')

    # ID of the note to be deleted
    note_id_to_delete = '12345'

    # Simulate the POST request
    response = client.post('/delete-note', data={'_id': note_id_to_delete})

    # Check that the response is a redirect (status code 302)
    assert response.status_code == 302

    # Verify that the mock delete_note_by_id function was called once with the correct ID
    mock_delete_note_by_id.assert_called_once_with(note_id_to_delete)


def test_get_search_route(client):
    response = client.get('/search')
    assert response.status_code == 200


def test_post_search_route(client):
    # Simulate POST request with a search query
    search_query = 'testQuery'
    post_response = client.post('/search', data={'search': search_query}, follow_redirects=True)

    # Verify the response after redirection
    # Checking if it redirects to the 'datasource' route with the correct query
    assert post_response.request.path == url_for('main.datasource', query=search_query)

    # Simulate GET request
    get_response = client.get('/search')

    # Verify that the GET request returns the correct template
    assert get_response.status_code == 200
