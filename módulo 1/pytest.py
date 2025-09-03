import pytest
from api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_soma_api(client):
    response = client.get('/soma/5/3')
    assert response.status_code == 200
    assert response.json['resultado'] == 8

def test_divide_api_sucesso(client):
    response = client.get('/divide/10/2')
    assert response.status_code == 200
    assert response.json['resultado'] == 5.0

def test_divide_api_por_zero(client):
    response = client.get('/divide/10/0')
    assert response.status_code == 400
    assert response.json['erro'] == "Não é possível dividir por zero."
