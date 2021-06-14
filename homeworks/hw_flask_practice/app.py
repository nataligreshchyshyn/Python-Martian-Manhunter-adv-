from flask import Flask, render_template, request, Response
import requests
from config import Config
from time import time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search_weather():
    cities_input = request.form.get("city_list")
    lat = request.form.get("lat")
    lon = request.form.get("lon")
    unix_time = str(int(time()))

    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST
    }

    responses = []
    if cities_input:
        cities = cities_input.split(',')
        for city in cities:
            querystring_city = {"q": city, "cnt": "1", "mode": "null", "lon": "0", "type": "link, accurate", "lat": "0",
                                "units": "metric"}
            city_info = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring_city)
            responses.append(city_info)
    else:
        querystring_location = {"lat": lat, "lon": lon, "dt": unix_time}
        loc_response = requests.request("GET", Config.WEATHER_API_TIMEMACHINE_URL, headers=headers,
                                        params=querystring_location)
        responses.append(loc_response)

    all_weather = []
    for response in responses:
        if response.status_code == 200:
            all_data = response.json()
            weather = {}
            if all_data.get("current"):
                weather["name"] = all_data["timezone"]
                weather["coord"] = {"lat": all_data["lat"], "lon": all_data["lon"]}
                weather["temp"] = int(all_data["current"]["temp"] - 273.15)
                weather["humidity"] = all_data["current"]["humidity"]
                weather["description"] = all_data["current"]["weather"][0]["description"]
                weather["clouds"] = all_data["current"]["clouds"]
                if all_data["current"].get("rain"):
                    weather["rain"] = True
            elif all_data.get("list"):
                weather["name"] = all_data["list"][0]["name"]
                weather["coord"] = all_data["list"][0]["coord"]
                weather["temp"] = all_data["list"][0]["main"]["temp"]
                weather["humidity"] = all_data["list"][0]["main"]["humidity"]
                weather["description"] = all_data["list"][0]["weather"][0]["description"]
                weather["clouds"] = all_data["list"][0]["clouds"]["all"]
                if all_data["list"][0].get("rain"):
                    weather["rain"] = True
            all_weather.append(weather)
        else:
            return Response(status=404)

    for item in all_weather:
        if not item:
            all_weather.remove(item)

    return render_template("weather.html", all_weather=all_weather)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
