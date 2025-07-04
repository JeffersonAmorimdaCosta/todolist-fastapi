from http import HTTPStatus

from fastapi.testclient import TestClient

from todolist_fastapi.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Message': 'Hello world!'}
