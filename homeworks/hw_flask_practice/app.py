# flask_web/app.py
from flask import Flask, render_template, request, Response
import requests
from config import Config
from time import time
from pprint import pprint

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search_weather():
    city = request.form.get("city")
    lat = request.form.get("lat")
    lon = request.form.get("lon")
    unix_time = str(int(time()))
    print(unix_time)



    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST
    }

    if city:
        querystring_city = {"q": city, "lat": "0", "lon": "0", "id": "0", "lang": "null",
                            "units": "metric", "mode": "xml, html"}
        response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring_city)
    else:
        querystring_location = {"lat": lat, "lon": lon, "dt": unix_time}
        response = requests.request("GET", Config.WEATHER_API_TIMEMACHINE_URL, headers=headers,
                                    params=querystring_location)

    if response.status_code == 200:
        weather = response.json()
        pprint(weather)
        return render_template("weather.html", weather=weather)
    # elif response.status_code == 200:
    #     weather = response.json()
    #     pprint(weather)
    #     return render_template("weather.html", weather=weather)
    else:
        return Response(status=404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
