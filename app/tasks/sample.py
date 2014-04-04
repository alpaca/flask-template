# -*- coding: utf-8 -*-

from app.tasks import celery

@celery.task(name='addition')
def addition(x, y):
	return x + y