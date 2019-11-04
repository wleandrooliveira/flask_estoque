import os
import random, string

class Config(object):
    CSRF_ENABLE = True
    SECRET = 'ysb_92=qe#djf8%ng+a*#4rt#5%3*4k5%i2bck*gn@w3@f&-&'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    SQLALCHEMY_DATABASE_URI ='mysql+mysqldb://raziel:quimica7295@localhost:3306/livro_flask'
    SENDGRID_API_KEY ='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'

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST =  8000
    URL_MAIN = 'http://%s:%s/' %(IP_HOST, PORT_HOST)

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST =  5000
    URL_MAIN = 'http://%s:%s/' %(IP_HOST, PORT_HOST)

class ProductConfig(Config):
    TESTING = False
    DEBUG = False
    IP_HOST = 'localhost'
    PORT_HOST =  8080
    URL_MAIN = 'http://%s:%s/' %(IP_HOST, PORT_HOST)

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductConfig()
}

app_active = os.getenv('FLASK_ENV')

