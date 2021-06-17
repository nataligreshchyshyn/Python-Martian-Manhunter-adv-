import pytest
from flask import request


def test_weather_info(client, mocker, fake_weather):
    weather_request = mocker.Mock()
    weather_request.json = mocker.Mock(return_value=fake_weather)
    weather_request.status_code = 200
    mocker.patch("requests.get", url="http://api.openweathermap.org/data/2.5/weather", return_value=weather_request)
    response = client.get('/weather?city=lviv,london')
    data = response.json
    assert request.path == "/weather"
    assert "lviv" in request.args["city"]
    assert response.status_code == 200
    assert data[0]["Lviv"]["name"] == "Lviv"
    assert data[1]["London"]["name"] == "London"
    weather_request.json = None
    weather_request.status_code = 404
    mocker.patch("requests.get", url="http://api.openweathermap.org/data/2.5/weather", return_value=weather_request)
    response = client.get('/weather?city=')
    data = response.json
    assert response.status_code == 404
    with pytest.raises(TypeError):
        assert data[0]["Lviv"]["name"] == "Lviv"
