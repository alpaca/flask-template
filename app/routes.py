# -*- coding: utf-8 -*-

from . import app
from .tasks import celery
from flask import render_template, request, redirect

from app.tasks.addition import addition

@app.route('/')
def root():
	return "Hello Alpaca"

@app.route('/moritz')
def moritz():
	return str(celery.send_task("add", args=[1,2]).get())

@app.route('/al')
def al():
	thing = addition.apply_async(args=[1,2])
	print thing
	return str(thing)
	# return str(celery.send_task("addition", args=[1,2]).get())