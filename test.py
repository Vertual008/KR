import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    rv = client.get('/')
    assert rv.data == b"Privet!"


def test_add(client):
    rv = client.get('/add?a=2&b=3')
    assert rv.json == {"result": 5.0}


def test_subtract(client):
    rv = client.get('/subtract?a=5&b=3')
    assert rv.json == {"result": 2.0}
