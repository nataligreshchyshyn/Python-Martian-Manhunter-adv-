from app import db


def autocommit(obj):
    with db.session.begin():
        db.session.add(obj)
