from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)

class people(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    lastname = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    address = db.Column(db.VARCHAR,nullable=True)
    reference_address = db.Column(db.VARCHAR,nullable=True)
    phone_number = db.Column(db.String(20),nullable=True)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}