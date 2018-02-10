import os
from information import *

HOME = '/tmp'
HOME = os.environ.get('LOG_HOME') or HOME
LOG_DIR = 'myapp'
LOG_FILE = 'myapp.log'
DEBUG_LOG_FILE = 'myapp_debug.log'
ERROR_LOG_FILE = 'myapp_error.log'
DB_FILE = 'myapp_db.log'
PORT = 5000
APP_NAME = 'myapp'

class Config:
	DEBUG = False
	TESTING = False
	API_TIMEOUT = 5
	def __init__(self):
		pass

	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
    HOME = '/tmp'
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+DB_USER+":"+DB_PASSWORD+'@'+DB_INSTANCE+'/'+DB_DATABASE
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS=True


class ProductionConfig(Config):
    HOME = '/var/log/'
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+DB_USER+":"+DB_PASSWORD+'@'+DB_INSTANCE+'/'+DB_DATABASE

config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}
# This is Archit Chauhans


