from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from app.people.models import app, db
from app.people.api import persona, personas
api = Api(app)



### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '../static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###




api.add_resource(personas, '/people')
api.add_resource(persona, '/people/<int:id>')

with app.app_context():
    db.create_all()


'''
if __name__ == '__main__':
    
    db.create_all()
    app.run(debug = True)
'''
