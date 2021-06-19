from app import app, api
from flask import render_template
from config import Config, articles, foot_cat
from flask_restful import Resource


@app.route('/', methods=["GET"])
def homepage():
    return render_template('blog/index.html', config=Config, articles=articles(), foot_cat=foot_cat())


class MenuItem(Resource):
    def get(self):
        return {
            'success': True,
            'items': Config.MENU_ITEMS
        }


class FooterLink(Resource):
    def get(self):
        return {
            'success': True,
            'items': Config.FOOTER_LINKS
        }


api.add_resource(MenuItem, '/menu-items')
api.add_resource(FooterLink, '/footer-useful-links')
