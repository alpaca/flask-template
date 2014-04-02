Summary
------------------
This flask-template allows you to easily deploy distributed applications.


Getting Started
------------------
Install RabbitMQ (We use RabbitMQ but the template supports any ampq implementation)
http://www.rabbitmq.com/download.html

Install dependencies. From a terminal inside the template folder.
```shell
sudo pip install -r requirements.txt
```

Initalize Database
```shell
python manage.py db init
```

Edit configuration/connection/logging settings in the "alembic.ini" file inside the migrations folder before proceeding. More info at : http://alembic.readthedocs.org/en/latest/tutorial.html#editing-the-ini-file

Create models in the "app/models" directory. More info at: https://pythonhosted.org/Flask-SQLAlchemy/models.html

Then run
```shell
python manage.py db migrate
```

Development Setup
------------------

```shell
mkvirtualenv app
pip install -r requirements.txt
honcho start
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