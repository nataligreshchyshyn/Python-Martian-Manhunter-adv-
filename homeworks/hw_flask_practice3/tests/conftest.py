import pytest
from app import app, db
from datetime import datetime


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.testing = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
    client = app.test_client()
    yield client


@pytest.fixture
def user():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
    with app.app_context():
        from models.models import Article, User
        db.create_all()

        user_test = User(
            username="test_user",
            email="test_u2@email.com",
            bio="about test user bla bla",
            created=datetime.now(),
            admin=1
        )

        db.session.query(User).delete()
        db.session.query(Article).delete()
        db.session.add(user_test)
        db.session.commit()

    yield "Test db is ready"


@pytest.fixture
def context():
    with app.test_request_context() as context:
        yield context
