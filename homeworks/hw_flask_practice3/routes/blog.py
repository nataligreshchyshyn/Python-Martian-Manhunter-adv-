import os
from app import app, api, db
from flask import render_template, request, Response, redirect
from config import Config, articles
from flask_restful import Resource, Api
from models.models import Article, User
from datetime import datetime


@app.route('/', methods=["GET"])
def homepage():
    articles = Article.query.all()
    return render_template('blog/index.html', config=Config, articles=articles)


@app.route('/article/<string:slug>')
def article_details(slug):
    article = Article.query.filter_by(slug=slug).first()
    return render_template('blog/article_details.html', article=article)


@app.route('/article/create')
def article_create():
    return render_template('blog/article_create.html')


@app.route('/article/store', methods=["POST"])
def article_store():
    data = request.form
    img = request.files['img']
    if img:
        path = "/" + Config.UPLOAD_PATH + img.filename
        img.save(os.path.join(Config.UPLOAD_PATH, img.filename))

        article = Article(
            author_id=1,
            title=data.get('title'),
            slug=data.get('slug'),
            description=data.get('description'),
            short_description=data.get('short_description'),
            img=path
        )
        db.session.add(article)
        db.session.commit()
        return redirect("/")
    else:
        return Response("Please, upload an image first", status=400)


@app.route('/user/create')
def user_create():
    return render_template('blog/user_create.html')


@app.route('/user/store', methods=["POST"])
def user_store():
    data = request.form
    print(data.get('admin'))
    print(type(data.get('admin')))
    user = User(
        username=data.get('username'),
        email=data.get('email'),
        created=str(datetime.now()),
        bio=data.get('bio'),
        admin=bool(int(data.get('admin')))
    )
    try:
        db.session.add(user)
        db.session.commit()
        return redirect("/user/create")
    except Exception:
        return Response("The user with the same data already exist in db", status=404)
