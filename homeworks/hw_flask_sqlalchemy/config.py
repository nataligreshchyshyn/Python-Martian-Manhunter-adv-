import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    BLOG_TITLE = "Blog Cursor"
    MENU_ITEMS = [
        {
            'name': "Articles",
            'link': '/articles',
        },
        {
            'name': "Categories",
            'link': '/categories',
        },
    ]


def articles():
    return [
        {
            "title": "Test Article",
            "img": "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
            "short_description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla blabla bla bla bla bla bla bla",
            "slug": 'test-article'
        },
        {
            "title": "Test Article2",
            "img": "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
            "short_description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla blabla bla bla bla bla bla bla",
            "slug": 'test-article2'
        },
    ]


def check_user(id):
    user = User.query.get(id)
    username = user.serialize["username"]
    return username
