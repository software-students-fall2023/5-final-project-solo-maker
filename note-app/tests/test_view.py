import pytest
from flask import url_for
from src import create_app
from src.models import mongo, get_notes, save_note, delete_note_by_id
from config import TestingConfig


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    mongo.init_app(app)

    with app.app_context():
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
    fake_note_id = "123"
    fake_note = {'_id': fake_note_id, 'title': 'Test Note', 'description': 'Test Description'}
    mocker.patch('src.views.get_note_by_id', return_value=fake_note)

    response = client.get(f'/edit-note?form={fake_note_id}')

    assert response.status_code == 200

    assert b'Test Note' in response.data
    assert b'Test Description' in response.data


def test_post_edit_note_route(client, mocker):
    mock_update_note_by_id = mocker.patch('src.views.update_note_by_id')

    response = client.post('/edit-note', data={'_id': '123', 'title': 'Test Note', 'description': 'Test Description'})
    assert response.status_code == 302
    mock_update_note_by_id.assert_called_once_with('123', 'Test Note', 'Test Description')


def test_post_delete_note_route(client, mocker):
    mock_delete_note_by_id = mocker.patch('src.views.delete_note_by_id')

    note_id_to_delete = '12345'

    response = client.post('/delete-note', data={'_id': note_id_to_delete})

    assert response.status_code == 302
    mock_delete_note_by_id.assert_called_once_with(note_id_to_delete)


def test_get_search_route(client):
    response = client.get('/search')
    assert response.status_code == 200


def test_post_search_route(client):
    search_query = 'testQuery'
    post_response = client.post('/search', data={'search': search_query}, follow_redirects=True)

    assert post_response.request.path == url_for('main.datasource', query=search_query)

    get_response = client.get('/search')

    assert get_response.status_code == 200
