from tests.conftest import fake_weather, client


def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200


def test_search_weather(client, mocker, fake_weather):

    weather_resp = mocker.Mock()
    weather_resp.json = mocker.Mock(return_value=fake_weather)
    weather_resp.status_code = 200
    mocker.patch("requests.request", url="https://community-open-weather-map.p.rapidapi.com/weather",
                 return_value=weather_resp)
    response = client.post("/search", data={"city": "lviv"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for Lviv" in response.data


