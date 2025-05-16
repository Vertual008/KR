import pytest
from tasklist import app  # Убедитесь, что tasklist.py в той же директории


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Тест главной страницы"""
    response = client.get('/')
    assert response.status_code == 200
