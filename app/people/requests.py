from flask_restful import reqparse

people_post_put_args = reqparse.RequestParser()
people_post_put_args.add_argument("name",type=str, help="Name is required",required=True)
people_post_put_args.add_argument("lastname",type=str, help="Last name is required",required=True)
people_post_put_args.add_argument("email",type=str, help="Email is required",required=True)
people_post_put_args.add_argument("address",type=str,required=False)
people_post_put_args.add_argument("reference_address",type=str,required=False)
people_post_put_args.add_argument("phone_number",type=str,required=False)

