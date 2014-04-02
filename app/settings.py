import os

class Config(object):
    DEBUG = False
    TESTING = False
    CELERY_RESULT_BACKEND = 'amqp'
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TIMEZONE = 'US/Central'
    CELERY_ENABLE_UTC = True

class Development(Config):
    DEBUG = True
    DATABASE_URL = 'development_db'
    BROKER_URL = 'amqp://'

class Production(Config):
    DATABASE_URL = os.getenv('DATABASE_URL')
    BROKER_URL = os.getenv('RABBITMQ_URL')

environment = os.environ.get('FLASK_ENV', 'development')
config = eval(environment.title())