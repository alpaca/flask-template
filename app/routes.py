from app import app
from flask import render_template, request, redirect

@app.route('/')
def root():
	return "Hello Alpaca"
