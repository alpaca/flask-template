```shell
python manage.py db init
```

create models and then

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