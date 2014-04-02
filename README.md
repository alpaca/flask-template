Summary
------------------
This flask-template allows you to easily deploy distributed applications.


Getting Started
------------------
Install RabbitMQ (We use RabbitMQ but the template supports any ampq implementation)
http://www.rabbitmq.com/download.html

Development Setup
------------------

```shell
mkvirtualenv app
pip install -r requirements.txt #install dependencies
python manage.py db init #initialize database
honcho --env=.secret start
# FLASK_ENV=production honcho --env=.secret start # production mode
# foreman --env=.secret start # using ruby foreman instead of honcho
```
Edit configuration/connection/logging settings in the "alembic.ini" file inside the migrations folder before proceeding. 
More info at : http://alembic.readthedocs.org/en/latest/tutorial.html#editing-the-ini-file

Create models in the "app/models" directory. 
More info at: https://pythonhosted.org/Flask-SQLAlchemy/models.html

After Creating Models
-------------------------
```shell
python manage.py db migrate
```

Production Setup
------------------

Dokku
```shell
dokku config:set HEROKU=1
dokku config:set C_FORCE_ROOT=true
```

Heroku
```shell
heroku config:set HEROKU=1
heroku config:set C_FORCE_ROOT=true
```

Dokku Specific Instructions
-----------------------------
Dokku requires setting the RABBITMQ_URL manually.
```
dokku config:set RABBITMQ_URL='amqp://USER:PASS@GATEWAY:PORT
```