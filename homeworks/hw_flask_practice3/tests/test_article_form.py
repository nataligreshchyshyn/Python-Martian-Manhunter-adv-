from tests.conftest import client, user, context
import pytest
import io
from requests_toolbelt import MultipartEncoder
from flask import request


def test_article_create(client):
    rv = client.get('/article/create')
    assert rv.status_code == 200
    html_data = rv.get_data()
    assert b"Cursor" in html_data
    assert b"Save" in html_data


def test_article_store(client, user, context):
    assert "Test db is ready" == user

    m_form = MultipartEncoder(fields={
        "title": "article_test",
        "slug": "a_test",
        "description": "test description bla bla bla bla bbld bla bla bla bla bla bla bla bla bla bla bla bla bla bla",
        "short_description": "test short description bla bla",
        "img": ("Screenshot from 2021-06-24 03-51-06.png", io.StringIO(), "image/jpg")
    })

    headers = {'Content-Type': m_form.content_type}

    rv = client.post('/article/store', headers=headers, data=m_form, follow_redirects=True)

    assert rv.status_code == 200
    assert b"test short description" in rv.data
    assert b"<title>Cursor Blog | Cursor</title>" in rv.data

    with context:
        assert request.path == "/"


def test_delete_article(client):
    response = client.delete("/api/articles/1")
    assert response.status_code == 204
    response = client.get("/api/articles/1")
    assert response.status_code == 404
