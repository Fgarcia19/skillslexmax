from flask_restful import Resource
from app.people.models import people
from app.people.requests import people_post_put_args


class personas(Resource):
    def get(self):
            try:
                all_people = people.query.all()
                json_allpeople = []
                for c in all_people:
                    json_allpeople.append(c.as_dict())
                return json_allpeople, 200
            except:
                return { 'Status':'500', 'Message':'Interal Server Error'},500

    def post(self):
        args = people_post_put_args.parse_args()
        print(args)
        try:
            new_person = people(name=args["name"],lastname=args["lastname"],email=args["email"],address=args["address"],reference_address=args["reference_address"],phone_number=args["phone_number"])
            new_person.save()
            return { 'Status':'200', 'Message':'New user created'},200
        except:
            return { 'Status':'500', 'Message':'Interal Server Error'},500
      
            

class persona(Resource):
    def get(self,id):
        try:
            person = people.query.filter_by(id=id).first()
            return person.as_dict()
        except:
            return { 'Status':'404', 'Message':'Not Found'}, 404
            

    def put(self,id):
        args = people_post_put_args.parse_args()
        try:
            name=args["name"]
            lastname=args["lastname"]
            email=args["email"]
            address=args["address"]
            reference_address=args["reference_address"]
            phone_number=args["phone_number"]
            person = people(name,lastname,email,address,reference_address,phone_number)
            person.update(id)
            return person.as_dict()
        except:
            return { 'Status':'500', 'Message':'Interal Server Error'}, 500


    def delete(self,id):
        try:
            person = people.delete(id)

            return { 'Status':'200', 'Message':'User deleted'}, 200
        except:
            return { 'Status':'500', 'Message':'Interal Server Error'},500
            