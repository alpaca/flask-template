# -*- coding: utf-8 -*-

import os
import logging

BROKER_SCHEME = os.getenv('BROKER_SCHEME', None)
BROKER_USERNAME = os.getenv('BROKER_USERNAME', "")
BROKER_PASSWORD = os.getenv('BROKER_PASSWORD', "")
BROKER_AMQP_PORT = os.getenv('BROKER_AMQP_PORT', "")
BROKER_ADMIN_PORT = os.getenv('BROKER_ADMIN_PORT', "")
BROKER_HOST = os.getenv('BROKER_HOST', "")
BROKER_PATH = os.getenv('BROKER_PATH', "")
BROKER_PORT_15672_TCP_PORT = os.getenv('BROKER_PORT_15672_TCP_PORT', "")
BROKER_PORT_5672_TCP_PORT = os.getenv('BROKER_PORT_5672_TCP_PORT', "")
BROKER_PORT_5672_TCP_ADDR = os.getenv('BROKER_PORT_5672_TCP_ADDR', "")

# logging.warn("BROKER_SCHEME: " + str(BROKER_SCHEME))
# logging.warn("BROKER_USERNAME: " + str(BROKER_USERNAME))
# logging.warn("BROKER_PASSWORD: " + str(BROKER_PASSWORD))
# logging.warn("BROKER_AMQP_PORT: " + str(BROKER_AMQP_PORT))
# logging.warn("BROKER_ADMIN_PORT: " + str(BROKER_ADMIN_PORT))
# logging.warn("BROKER_HOST: " + str(BROKER_HOST))
# logging.warn("BROKER_PATH: " + str(BROKER_PATH))
# logging.warn("BROKER_PORT_15672_TCP_PORT: " + str(BROKER_PORT_15672_TCP_PORT))
# logging.warn("BROKER_PORT_5672_TCP_PORT: " + str(BROKER_PORT_5672_TCP_PORT))
# logging.warn("BROKER_PORT_5672_TCP_ADDR: " + str(BROKER_PORT_5672_TCP_ADDR))

# logging.warn(os.environ)

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:postgres@localhost:5432/app_development')    
    # BROKER_URL = os.getenv('RABBITMQ_URL', 'amqp://')

    if BROKER_SCHEME is not None:
        BROKER_URL = BROKER_SCHEME + '://' + BROKER_USERNAME + ':' + BROKER_PASSWORD + '@' + BROKER_HOST + ':' + BROKER_ADMIN_PORT + BROKER_PATH
    else:
        BROKER_URL = 'amqp://'

    logging.warn(BROKER_URL)

    CELERY_RESULT_BACKEND = 'amqp'
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TIMEZONE = 'US/Central'
    CELERY_ENABLE_UTC = True
    CELERY_REDIRECT_STDOUTS = True
    CELERY_REDIRECT_STDOUTS_LEVEL = 'DEBUG'
    CELERY_TRACK_STARTED = True

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