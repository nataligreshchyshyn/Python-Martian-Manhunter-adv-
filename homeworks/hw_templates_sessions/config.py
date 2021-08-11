import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    UPLOAD_PATH = 'static/uploads/'
    BLOG_TITLE = "Blog Cursor"
    MENU_ITEMS = [
        {
            'name': "Articles",
            'link': '/api/articles',
        },
        {
            'name': "Categories",
            'link': '/api/categories',
        },
    ]
