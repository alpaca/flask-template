# -*- coding: utf-8 -*-

import os
import logging


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:postgres@localhost:5432/app_development')    
    # BROKER_URL = os.getenv('RABBITMQ_URL', 'amqp://')

    BROKER_SCHEME = os.getenv('BROKER_SCHEME', None)
    BROKER_USERNAME = os.getenv('BROKER_USERNAME', None)
    BROKER_PASSWORD = os.getenv('BROKER_PASSWORD', None)
    BROKER_PORT = os.getenv('BROKER_PORT', None)
    BROKER_HOST = os.getenv('BROKER_HOST', None)
    BROKER_PATH = os.getenv('BROKER_PATH', None)
    BROKER_PORT_15672_TCP_PORT = os.getenv('BROKER_PORT_15672_TCP_PORT', None)
    BROKER_PORT_5672_TCP_PORT = os.getenv('BROKER_PORT_5672_TCP_PORT', None)
    BROKER_PORT_5672_TCP_ADDR = os.getenv('BROKER_PORT_5672_TCP_ADDR', None)

    print "BROKER_SCHEME: " + str(BROKER_SCHEME)
    print "BROKER_USERNAME: " + str(BROKER_USERNAME)
    print "BROKER_PASSWORD: " + str(BROKER_PASSWORD)
    print "BROKER_PORT: " + str(BROKER_PORT)
    print "BROKER_HOST: " + str(BROKER_HOST)
    print "BROKER_PATH: " + str(BROKER_PATH)
    print "BROKER_PORT_15672_TCP_PORT: " + str(BROKER_PORT_15672_TCP_PORT)
    print "BROKER_PORT_5672_TCP_PORT: " + str(BROKER_PORT_5672_TCP_PORT)
    print "BROKER_PORT_5672_TCP_ADDR: " + str(BROKER_PORT_5672_TCP_ADDR)

    # logging.warning(BROKER_SCHEME)
    # logging.warning(BROKER_USERNAME)
    # logging.warning(BROKER_PASSWORD)
    # logging.warning(BROKER_PORT)
    # logging.warning(BROKER_HOST)
    # logging.warning(BROKER_PATH)
    # logging.warning(BROKER_PORT_15672_TCP_PORT)
    # logging.warning(BROKER_PORT_5672_TCP_PORT)
    # logging.warning(BROKER_PORT_5672_TCP_ADDR)

    if BROKER_SCHEME is not None:
        BROKER_URL = BROKER_SCHEME + '://' + BROKER_USERNAME + ':' + BROKER_PASSWORD + '@' + BROKER_HOST + ':' + BROKER_PORT + BROKER_PATH
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