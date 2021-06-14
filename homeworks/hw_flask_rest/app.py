from flask import Flask, render_template, request, Response
from flask_restful import Resource, Api
import requests
from config import Config

app = Flask(__name__)

api = Api(app)

todos = {}
weather_info = {}


class Todo(Resource):

    def get(self, todo_id):
        try:
            data = {todo_id: todos[todo_id]}
        except KeyError:
            return Response("Not found", status=404)
        return data

    def put(self, todo_id):
        todos[todo_id] = request.json.get("text")
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        del todos[todo_id]
        return Response(todos, status=204)


class TodoList(Resource):

    def get(self):
        return todos

    def post(self):
        todos[request.json.get("todo_id", None)] = request.json.get("text", "")
        return todos


class Weather(Resource):

    def get(self):
        cities = request.args.get("city")
        city_list = cities.split(",")

        headers = {
            "x-rapidapi-key": Config.WEATHER_API_KEY,
            "x-rapidapi-host": Config.WEATHER_API_HOST
        }

        for city in city_list:
            querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "0", "type": "link, accurate", "lat": "0",
                           "units": "metric"}

            response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)

            if response.status_code == 200:
                weather = response.json()
                weather_info[f"{city}"] = weather
            else:
                return Response(status=404)
        return weather_info


api.add_resource(Todo, "/todos/<int:todo_id>")
api.add_resource(TodoList, "/todos")
api.add_resource(Weather, "/weather")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
