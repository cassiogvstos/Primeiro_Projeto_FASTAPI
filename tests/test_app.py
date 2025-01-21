from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retorna_ok_e_ola_mundo():
# Arrange (Organização do teste)  # noqa: E115
    client = TestClient(app)
    # Act (Ação do teste)
    response = client.get('/')
    # assert (Garantindo que o status code é o que queremos)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
