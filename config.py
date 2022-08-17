from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')