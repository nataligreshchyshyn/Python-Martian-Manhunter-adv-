import os
import datetime

from sqlalchemy.exc import IntegrityError

from app import app, db
from flask import render_template, request, redirect, session, flash
from config import Config

from helpers.autocommit import autocommit
from models.models import Article, User
from helpers.additional_functions import check_password


@app.route('/', methods=["GET"])
def homepage():
    articles = Article.query.all()
    session['hello'] = 'hello world'
    return render_template('blog/index.html', config=Config, articles=articles)


@app.route('/sign-up', methods=['GET'])
def sign_up():
    if session.get('user', False):
        return redirect('/')
    return render_template('blog/signup.html')


@app.route('/user-register', methods=['POST'])
def user_store():
    data = request.form
    try:
        user = User(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'),
            bio=data.get('description'),
            created=datetime.datetime.now(),
            admin=0,
        )

        autocommit(user)

        session['user'] = user.serialize
        return redirect("/")
    except IntegrityError:
        db.session.rollback()
        flash(f"ERROR! Email ({data.get('email')}) already exists.", "error")
        return redirect("/sign-up")


@app.route('/sign-in', methods=['GET'])
def sign_in():
    if session.get('user', False):
        return redirect('/')
    return render_template('blog/signin.html')


@app.route('/login', methods=['POST'])
def login():
    user = User.query.filter_by(email=request.form.get('username')).first()
    if user:
        if check_password(user.password, request.form.get('password')):
            session['user'] = user.serialize
            return redirect("/")
        else:
            flash(f"Incorrect username/password combination. Please, try again", "error")
            return redirect("/sign-in")

    else:
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user:
            if check_password(user.password, request.form.get('password')):
                session['user'] = user.serialize
                return redirect("/")
            else:
                flash(f"Incorrect username/password combination. Please, try again", "error")
                return redirect("/sign-in")
    flash(f"User doesn't exist. Please, sign up first.")
    return redirect("/sign-up")


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user')
    return redirect('/')


@app.route('/article/<string:slug>')
def article_details(slug):
    article = Article.query.filter_by(slug=slug).first()
    return render_template('blog/details.html', article=article)


@app.route('/article/create')
def article_create():
    if not session.get('user', False):
        return redirect('/')
    return render_template('blog/article_create.html')


@app.route('/contact-us')
def contact_us():
    return render_template('blog/contact-us.html')


@app.route('/article/store', methods=["POST"])
def article_store():
    if not session.get('user', False):
        return redirect('/')
    data = request.form
    img = request.files['img']
    if img:
        img.save(os.path.join(Config.UPLOAD_PATH, img.filename))
        path = "/" + Config.UPLOAD_PATH + img.filename

    article = Article(
        title=data.get('title'),
        slug=data.get('slug'),
        author_id=1,
        description=data.get('description'),
        short_description=data.get('short_description'),
        img=path
    )

    autocommit(article)
    return redirect("/")