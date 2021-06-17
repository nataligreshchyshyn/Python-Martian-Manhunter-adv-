from tests.conftest import client, todos
import json


def test_create(client, todos):
    headers = {
        "Content-Type": "application/json"
    }
    response = client.post("/todos", headers=headers, json=todos)
    assert response.status_code == 200
    assert response.json['todo_id'] == 1
    assert response.json["text"] == "text1"


def test_list(client):
    headers = {
        "Content-Type": "application/json"
    }
    response = client.get('/todos')
    assert response.status_code == 200
    assert type(response.json) is list
    for x in response.json:
        assert type(x['todo_id']) is int
        assert type(x["text"]) is str


def test_update(client):
    update_data = {
        "text": "blablabla"
    }

    response = client.put("/todos/1", json=update_data)
    assert response.status_code == 200
    get_response = client.get("/todos/1")
    assert get_response.status_code == 200
    assert get_response.json['text'] == "blablabla"


def test_delete(client):
    response = client.delete("/todos/1")
    assert response.status_code == 204
    response = client.get("/todos/1")
    assert response.status_code == 404
