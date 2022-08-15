from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import json
import os
from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{os.getenv("DATABASE_USER")}:{os.getenv("DATABASE_PASSWORD")}@{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE_DB")}'
db = SQLAlchemy(app)

api = Api(app)


### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


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


class personas(Resource):
    def get(self):
            all_people = people.query.all()
            json_allpeople = []
            for c in all_people:
                json_allpeople.append(c.as_dict())
            return json_allpeople
    def post(self):
            data = request.get_json()
            name = data['name']
            lastname = data['lastname']
            email = data['email']
            address = ""
            reference_address = ""
            phone_number = ""
            if 'address' in data:
                address = data['address']
            if 'reference_address' in data:
                reference_address = data['reference_address']
            if 'phone_number' in data:
                phone_number = data['phone_number']
            new_person = people(name=name,lastname=lastname,email=email,address=address,reference_address=reference_address,phone_number=phone_number)
            db.session.add(new_person)
            db.session.commit()
            return { 'Status':'200', 'Message':'New user created'}

class persona(Resource):
    def get(self,id):
        person = people.query.filter_by(id=id).first()
        return person.as_dict()
    def put(self,id):
        person = people.query.filter_by(id=id).first()
        data = request.get_json()
        person.name = data['name']
        person.lastname = data['lastname']
        person.email = data['email']
        if 'address' in data:
            person.address = data['address']
        if 'reference_address' in data:
            person.reference_address = data['reference_address']
        if 'phone_number' in data:
            person.phone_number = data['phone_number']
        db.session.commit()
        return person.as_dict()
    def delete(self,id):
        person = people.query.filter_by(id=id).first()
        db.session.delete(person)
        db.session.commit()
        return { 'Status':'200', 'Message':'User deleted'}


api.add_resource(personas, '/people')
api.add_resource(persona, '/people/<int:id>')

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)

#TODO
    #requirements.txt
    #.gitignore