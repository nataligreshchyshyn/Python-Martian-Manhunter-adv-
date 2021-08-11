import os
import datetime
from app import app, db
from flask import render_template, request, redirect, session, flash
from config import Config, foot_cat
from models.models import Article, User
from helpers.confirm_email import send_confirmation_email
from sqlalchemy.exc import IntegrityError
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime


@app.route("/", methods=["GET"])
def homepage():
    articles = Article.query.all()
    session["hello"] = "hello world"
    return render_template("blog/index.html", config=Config, articles=articles, foot_cat=foot_cat())


@app.route("/sign-up", methods=["GET"])
def sign_up():
    if session.get("user", False):
        return redirect("/")
    return render_template("blog/signup.html")


@app.route("/user-register", methods=["POST"])
def user_store():
    data = request.form
    try:
        user = User(
            username=data.get("username"),
            email=data.get("email"),
            bio=data.get("description"),
            created=datetime.now(),
            admin=0,
            email_confirmation_sent_on=None,
            email_confirmed_on=None
        )
        user.set_password(data.get("password"))
        send_confirmation_email(user.email)
        user.email_confirmation_sent_on = datetime.now()

        db.session.add(user)
        db.session.commit()
        flash(f"Thanks for registering!  Please check your email to confirm your email address to activate your "
              f"account.", "success")
        return redirect("/")
    except IntegrityError:
        db.session.rollback()
        flash(f"ERROR! Email ({data.get('email')}) already exists.", "error")
        return redirect("/sign-up")


@app.route("/sign-in", methods=["GET"])
def sign_in():
    if session.get("user", False):
        return redirect("/")
    return render_template("blog/signin.html")


@app.route("/login", methods=["POST"])
def login():
    user = User.query.filter_by(email=request.form.get("username")).first()
    if user:
        if user.check_password(request.form.get("password")) and user.email_confirmed is True:
            session["user"] = user.serialize
            return redirect("/")
        elif user.check_password(request.form.get("password")) and user.email_confirmed is False:
            flash(f"Please, confirm your email to activate your account", "info")
            return redirect("/")
        else:
            flash(f"Incorrect username/password combination. Please, try again", "error")
            return redirect("/sign-in")
    else:
        user = User.query.filter_by(username=request.form.get("username")).first()
        if user:
            if user.check_password(request.form.get("password")) and user.email_confirmed is True:
                session["user"] = user.serialize
                return redirect("/")
            elif user.check_password(request.form.get("password")) and user.email_confirmed is False:
                flash(f"Please, confirm your email to activate your account", "info")
                return redirect("/")
            else:
                flash(f"Incorrect username/password combination. Please, try again", "error")
                return redirect("/sign-in")
    flash(f"User doesn't exist. Please, sign up first.")
    return redirect("/sign-up")


@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user")
    return redirect("/")


@app.route("/confirm/<token>")
def confirm_email(token):
    try:
        confirm_serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
        email = confirm_serializer.loads(token, salt="email-confirmation-salt", max_age=3600)
    except:
        flash(f"The confirmation link is invalid or has expired.", "error")
        return redirect("/")

    user = User.query.filter_by(email=email).first()

    if session.get("user") and user.email_confirmed:
        flash(f"Account already confirmed. Please, login with email {user.email}", "info")
        return redirect("/")
    elif user.email_confirmed:
        flash(f"Account already confirmed. Please login.", "info")
        return redirect("/sign-in")
    else:
        user.email_confirmed = True
        user.email_confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        session["user"] = user.serialize
        flash(f"Thank you for confirming your email address!", "success")
        return redirect("/")


@app.route("/article/<string:slug>")
def article_details(slug):
    article = Article.query.filter_by(slug=slug).first()
    return render_template("blog/details.html", article=article)


@app.route("/article/create")
def article_create():
    if not session.get("user", False):
        return redirect("/")
    return render_template("blog/article_create.html")


@app.route("/contact-us")
def contact_us():
    return render_template("blog/contact-us.html", foot_cat=foot_cat())


@app.route("/article/store", methods=["POST"])
def article_store():
    if not session.get("user", False):
        return redirect("/")
    data = request.form
    img = request.files["img"]
    if img:
        img.save(os.path.join(Config.UPLOAD_PATH, img.filename))
        path = "/" + Config.UPLOAD_PATH + img.filename

    article = Article(
        title=data.get("title"),
        slug=data.get("slug"),
        author_id=1,
        description=data.get("description"),
        short_description=data.get("short_description"),
        img=path
    )

    db.session.add(article)
    db.session.commit()
    return redirect("/")
