import pytest
from app import app
import json


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def todos():
    yield {
        "todo_id": 1,
        "text": "text1"
    }


@pytest.fixture
def fake_weather():
    with open('tests/resources/weather_sample.json') as f:
        return json.load(f)
