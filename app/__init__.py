# -*- coding: utf-8 -*-

import os, sys, logging
from flask import Flask
from . import settings

# Allow importing libraries from lib folder
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../lib')

app = Flask(__name__)
app.config.from_object(settings.config)

from . import models
from . import controllers
from . import routes

app.logger.addHandler(settings.log_handler)

if not app.debug:
    app.logger.setLevel(logging.INFO)
    log_handler.setLevel(logging.INFO)
else:
    app.logger.setLevel(logging.DEBUG)
    log_handler.setLevel(logging.DEBUG)