from .db import db


class User(db.Document):
    email = db.StringField(required=True)
    password = db.StringField(required=True)


class Questions(db.Document):
    statement = db.StringField(required=True)
    options = db.ListField(db.StringField())
    correct = db.IntField()



