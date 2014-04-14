# -*- coding: utf-8 -*-

from . import app
from .tasks import celery
from flask import render_template, request, redirect

def root():
	return "Hello Alpaca"

@app.route('/sample')
def sample():
	thing = celery.send_task("addition", args=[1,2], queue="celery")
	print thing
	return str(thing.get())