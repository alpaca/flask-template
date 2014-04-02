import os, sys
from app.settings import config
from flask import Flask

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../lib')

app = Flask(__name__)

app.config.from_object(config)

from app import models
from app import controllers
from app import routes