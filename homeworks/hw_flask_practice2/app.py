# flask_web/app.py
from flask import Flask, render_template, request, jsonify, Response
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

with app.app_context():
    import routes.blog

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
