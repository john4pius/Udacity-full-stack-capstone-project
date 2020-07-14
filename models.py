import os
from sqlalchemy import Column, String, create_engine, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import date

database_path = os.environ.get('DATABASE_URL')

if not database_path:
    database_name = "boxoffice"
    database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

    db.create_all()


def db_drop_and_create():
    db.drop_all()
    db.create_all()
    insert_seed_records()


def insert_seed_records():
    actor1 = Actor(name="Dwayne Johnson", age=54, gender="Male")
    actor1.insert()

    movie1 = Movie(title="Jumanji", release_date=date.today())
    movie1.insert()


class Movie(db.Model):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(db.DateTime, nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date
        }


class Actor(db.Model):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }
