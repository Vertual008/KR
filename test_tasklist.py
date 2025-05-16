import pytest


from tasklist import app  # Импорт после пустой строки


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Тест главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"To-Do List" in response.data


def test_get_tasks(client):
    """Тест получения задач"""
    response = client.get('/tasks')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
