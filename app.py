from flask import request
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
from models import people, app, db
from requests import people_post_put_args
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

class personas(Resource):
    def get(self):
            try:
                all_people = people.query.all()
                json_allpeople = []
                for c in all_people:
                    json_allpeople.append(c.as_dict())
                return json_allpeople
            except:
                return { 'Status':'500', 'Message':'Interal Server Error'}

    def post(self):
        args = people_post_put_args.parse_args()
        print(args)
        try:
            new_person = people(name=args["name"],lastname=args["lastname"],email=args["email"],address=args["address"],reference_address=args["reference_address"],phone_number=args["phone_number"])
            db.session.add(new_person)
            db.session.commit()
            return { 'Status':'200', 'Message':'New user created'}
        except:
            return { 'Status':'500', 'Message':'Interal Server Error'}
      
            

class persona(Resource):
    def get(self,id):
        try:
            person = people.query.filter_by(id=id).first()
            return person.as_dict()
        except:
            return { 'Status':'500', 'Message':'Interal Server Error'}
            

    def put(self,id):
        person = people.query.filter_by(id=id).first()
        args = people_post_put_args.parse_args()
        try:
            person.name=args["name"]
            person.lastname=args["lastname"]
            person.email=args["email"]
            person.address=args["address"]
            person.reference_address=args["reference_address"]
            person.phone_number=args["phone_number"]
            db.session.commit()
            return person.as_dict()
        except:
            return { 'Status':'500', 'Message':'Interal Server Error'}


    def delete(self,id):
        person = people.query.filter_by(id=id).first()
        try:
            db.session.delete(person)
            db.session.commit()
            return { 'Status':'200', 'Message':'User deleted'}
        except:
            return { 'Status':'500', 'Message':'Interal Server Error'}
            


api.add_resource(personas, '/people')
api.add_resource(persona, '/people/<int:id>')

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)

#TODO
    #requirements.txt
    #.gitignore