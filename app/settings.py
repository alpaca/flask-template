# -*- coding: utf-8 -*-

import os
import logging


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:postgres@localhost:5432/app_development')    
    # BROKER_URL = os.getenv('RABBITMQ_URL', 'amqp://')

    if os.getenv('BROKER_SCHEME', None) is not None:
        BROKER_URL = os.getenv('BROKER_SCHEME') + '://' + os.getenv('BROKER_USERNAME') + ':' + os.getenv('BROKER_PASSWORD') + '@' + os.getenv('BROKER_HOST') + ':' + os.getenv('BROKER_PORT') + os.getenv('BROKER_PATH')
    else:
        BROKER_URL = 'amqp://'

    CELERY_RESULT_BACKEND = 'amqp'
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TIMEZONE = 'US/Central'
    CELERY_ENABLE_UTC = True
    CELERY_REDIRECT_STDOUTS = True
    CELERY_REDIRECT_STDOUTS_LEVEL = 'DEBUG'
    CELERY_TRACK_STARTED = True

    print "BROKER_URL: " + BROKER_URL
    print "SQLALCHEMY_DATABASE_URI: " + SQLALCHEMY_DATABASE_URI
    logging.warning(BROKER_URL)

class Development(Config):
    DEBUG = True

class Production(Config):
    pass

environment = os.environ.get('FLASK_ENV', 'development')
config = eval(environment.title())

# Logging

from logging import Formatter, FileHandler, StreamHandler
formatter = Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')

log_handler = None
if environment != "production":
    log_handler = FileHandler('app.log') 
    log_handler.setFormatter(formatter)
else:
    log_handler = StreamHandler()
    log_handler.setFormatter(formatter)