import pytest
from app import app
import json


@pytest.fixture()
def fake_weather():
    with open('tests/resources/weather_sample.json') as f:
        return json.load(f)


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
