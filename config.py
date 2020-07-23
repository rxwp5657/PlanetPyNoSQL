from os     import environ, path
#from dotenv import load_dotenv

#basedir = path.abspath(path.dirname(__file__))
#load_dotenv(path.join(basedir, '.env'))

class Config:

    # app configuration
    FLASK_APP = environ.get("FLASK_APP", "default")
    FLASK_ENV = environ.get("FLASK_ENV", "production")

class DBConfig:
    # database configuration
    NAME = environ.get("DB_NAME") 
    USER = environ.get("DB_USER")
    HOST = environ.get("DB_HOST")
    PASSWORD = environ.get("DB_PASSWORD")