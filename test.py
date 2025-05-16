import pytest
from tasklist import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert isinstance(response.json['tasks'], list)


def test_add_task(client):
    test_data = {'task': 'Новая тестовая задача'}
    response = client.post('/add_task', json=test_data)
    assert response.status_code == 200
    assert 'Задача добавлена' in response.json['message']
