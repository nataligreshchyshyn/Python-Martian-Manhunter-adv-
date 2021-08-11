from itsdangerous import URLSafeTimedSerializer
from config import Config
from flask import url_for, render_template
from flask_mail import Message
from app import mail


def send_email(subject, recipients, text_body, html_body):
    msg = Message(subject, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def send_confirmation_email(user_email):
    confirm_serializer = URLSafeTimedSerializer(Config.SECRET_KEY)

    confirm_url = url_for(
        'confirm_email',
        token=confirm_serializer.dumps(user_email, salt='email-confirmation-salt'),
        _external=True
    )

    html = render_template(
        'blog/email_confirmation.html',
        confirm_url=confirm_url
    )

    body = 'Thanks for registering with Cursor Blog!'

    send_email('Confirm Your Email Address', [user_email], body, html)
