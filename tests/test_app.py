from http import HTTPStatus


def test_root_deve_retorna_ok_e_ola_mundo(client):
    # Arrange (Organização do teste)
    # Act (Ação do teste)
    response = client.get('/')
    # assert (Garantindo que o status code é o que queremos)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def teste_create_user(client):

    response = client.post(
        # UserSchema
        '/users/',
        json={
            'username': 'testeusername',
            'password': 'pass',
            'email': 'test@test.com',
        }
    )

    # Voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {
        'username': 'testeusername',
        'email': 'test@test.com',
        'id': 1
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [
        {
            'username': 'testeusername',
            'email': 'test@test.com',
            'id': 1
        }
    ]}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'testeusername2',
            'email': 'test@test.com',
            'id': 1
        }
    )
    assert response.json() == {
        'username': 'testeusername2',
        'email': 'test@test.com',
        'id': 1
    }


def test_get_user_should_return_not_found(client):
    response = client.get('/users/555')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deletede!'}
