from os import path

from flask import Flask, request, Response
from flask_restful import Resource, Api
import requests
from config import Config
import json

app = Flask(__name__)

api = Api(app)


class Todo(Resource):

    def get(self, todo_id):
        with open("/usr/src/app/todos.txt", "r") as f:
            todos = json.load(f)
            try:
                data = [x for x in todos if x["todo_id"] == todo_id][0]
            except IndexError:
                return Response("Not found", status=404)
        return data

    def put(self, todo_id):
        with open("/usr/src/app/todos.txt", "r") as f:
            todos = json.load(f)
            new_text = request.json.get("text")
            try:
                data = [todos.pop(todos.index(x)) for x in todos if x["todo_id"] == todo_id][0]
                data["text"] = new_text
                todos.append(data)
            except IndexError:
                return Response("Not found", status=404)
        with open("/usr/src/app/todos.txt", "w") as f:
            f.write(json.dumps(todos))
        return data

    def delete(self, todo_id):
        with open("/usr/src/app/todos.txt", "r") as f:
            todos = json.load(f)
            try:
                item_to_del = [x for x in todos if x["todo_id"] == todo_id][0]
                todos.remove(item_to_del)
            except IndexError:
                return Response("Not found", status=404)
        with open("/usr/src/app/todos.txt", "w") as f:
            f.write(json.dumps(todos))
        return Response(status=204)


class TodoList(Resource):

    def get(self):
        with open("/usr/src/app/todos.txt", "r") as f:
            todos = json.load(f)
        return todos

    def post(self):
        if not path.isfile("/usr/src/app/todos.txt"):
            with open("/usr/src/app/todos.txt", "w") as f:
                todos = {
                    "todo_id": request.json.get("todo_id", None),
                    "text": request.json.get("text", "")
                }
                f.write(json.dumps([todos]))
        else:
            with open("/usr/src/app/todos.txt", "r") as f:
                data = json.load(f)
                todos = {
                    "todo_id": request.json.get("todo_id", None),
                    "text": request.json.get("text", "")
                }
                data.append(todos)

            with open("/usr/src/app/todos.txt", "w") as f:
                f.write(json.dumps(data))

        return todos


class Weather(Resource):

    def get(self):
        weather_info = []

        cities = request.args.get("city")
        city_list = cities.split(",")

        for city in city_list:
            response = requests.get(Config.WEATHER_API_URL, params=dict(q=city, units="metric",
                                                                        APPID=Config.WEATHER_API_KEY))
            if response.status_code == 200:
                weather = response.json()
                weather_info.append(weather)
            else:
                return Response(status=404)
        return weather_info


api.add_resource(Todo, "/todos/<int:todo_id>")
api.add_resource(TodoList, "/todos")
api.add_resource(Weather, "/weather")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
