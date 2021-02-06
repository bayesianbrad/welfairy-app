
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    """Base Config"""
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    SECRET_KEY = os.getenv('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class ProductionConfig(Config):
    DEBUG=False
    TESTING=False
    FLASK_ENV='production'
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')

class DevelopmentConfig(Config):
    DEBUG=True
    TESTING=True
    FLASK_ENV='development'
    # FLASK_APP=app.py
    FLASK_DEBUG=1
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

