from app import app, api, db
from flask import render_template, request, Response
from config import Config, articles
from flask_restful import Resource, Api
from models.models import Article, User
from datetime import datetime
from sqlalchemy import update


@app.route('/', methods=["GET"])
def homepage():
    articles = Article.query.all()
    return render_template('blog/index.html', config=Config, articles=articles)


@app.route('/article/<string:slug>')
def article_details(slug):
    article = Article.query.filter_by(slug=slug).first()
    return render_template('blog/details.html', article=article, username=check_user(article.author_id))


def check_user(id):
    user = User.query.get(id)
    username = user.username
    return username


class MenuItem(Resource):
    def get(self):
        return {
            'success': True,
            'items': Config.MENU_ITEMS
        }


class Articles(Resource):
    def post(self):
        data = request.json
        article = Article(
            title=data.get('title'),
            slug=data.get('slug'),
            author_id=data.get('author_id'),
            description=data.get('description'),
            short_description=data.get('short_description'),
            img=data.get('img')
        )
        db.session.add(article)
        db.session.commit()
        return article.serialize

    def get(self):
        articles = Article.query
        if request.args.get('title'):
            articles = articles.filter_by(title=request.args.get('title'))

        # articles = articles.filter(Article.title.startswith('A'))

        if request.args.get("sort_by"):
            articles = articles.order_by(request.args.get("sort_by"))

        articles = articles.all()
        serialized_articles = []
        for article in articles:
            serialized_articles.append(article.serialize)

        return serialized_articles


class ArticleEntity(Resource):

    def get(self, id):
        article = Article.query.get(id)
        if article == None:
            return Response(status=404)
        return article.serialize


class Users(Resource):

    def post(self):
        data = request.json
        user = User(
            username=data.get('username'),
            email=data.get('email'),
            bio=data.get('bio'),
            created=str(datetime.now()),
            admin=data.get('admin'),
        )
        db.session.add(user)
        db.session.commit()
        return user.serialize

    def get(self):
        users = User.query

        if request.args.get("sort_by"):
            users = users.order_by(request.args.get("sort_by"))

        if request.args.get("id"):
            users = users.filter_by(id=request.args.get("id"))

        if request.args.get("name"):
            users = users.filter_by(username=request.args.get("name"))

        if request.args.get("is_admin"):
            users = users.filter_by(admin=request.args.get("is_admin"))

        all_users = users.all()
        serialized_users = []
        for user in all_users:
            serialized_users.append(user.serialize)

        return serialized_users


class UserEntity(Resource):

    def get(self, id):
        user = User.query.get(id)

        if user:
            return user.serialize
        else:
            return Response("There are no users with requested ID", status=500)

    def put(self, id):
        data = request.json
        keys = ["username", "email", "bio", "admin"]
        if data:
            try:
                user = User.query.filter_by(id=id)
                for k in data.keys():
                    if k in keys:
                        user.update({k: data[k], "created": str(datetime.now())})
                    else:
                        return Response("Incorrect data", status=404)
                db.session.commit()
                return User.query.get(id).serialize
            except AttributeError:
                return Response("There's no user with the requested ID", status=404)
        else:
            return Response("Please, enter info to update", status=404)

    def delete(self, id):
        user = User.query.get(id)

        if user is None:
            return Response("There's no user with the requested ID", status=404)

        db.session.delete(user)
        db.session.commit()

        return Response(status=204)


class UserArticles(Resource):

    def get(self, id):
        user = User.query.get(id)
        serialized_articles = []
        for article in user.articles:
            serialized_articles.append(article.serialize)
        return serialized_articles



api.add_resource(MenuItem, '/menu-items')
api.add_resource(Articles, '/articles')
api.add_resource(Users, '/users')
api.add_resource(UserEntity, '/users/<int:id>')
api.add_resource(UserArticles, '/users/articles/<int:id>')
api.add_resource(ArticleEntity, '/articles/<int:id>')
