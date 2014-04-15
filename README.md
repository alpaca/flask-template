Summary
------------------
This flask-template allows you to easily deploy distributed applications.

Getting Started
------------------
Install RabbitMQ (We use RabbitMQ but the template supports any ampq implementation)
http://www.rabbitmq.com/download.html

Development Setup
------------------

```bash
mkvirtualenv app
pip install -r requirements.txt #install dependencies
python manage.py db init #initialize database
touch .secret
honcho start -e .secret
foreman start -e .secret # alternative ruby version
```

Add FLASK_ENV=production before honcho/foreman to run in 'production' mode

If running honcho or foreman and both processes fail to start, you may 
end up with several different versions of a single process running. Use
a variation of the command below to stop them.

```bash
ps aux | egrep 'celery worker|python manage|gunicorn|flower' | grep -v grep | awk '{print $2}' | xargs kill -9
```

Use this to detect whether the processes are running.
```bash
ps aux | egrep 'gunicorn|celery|manage.py'
```

Edit configuration/connection/logging settings in the "alembic.ini" file inside the migrations folder before proceeding. 
More info at : http://alembic.readthedocs.org/en/latest/tutorial.html#editing-the-ini-file

Create models in the "app/models" directory. 
More info at: https://pythonhosted.org/Flask-SQLAlchemy/models.html


Git Submodules
---------------
As you're developing non-domain specific python packages, you should use git submodules to add them to the lib folder. See this stackoverflow for how to do that: http://stackoverflow.com/questions/9189575/git-submodule-tracking-latest

Using git submodules helps you easily go back and forth between both codebases.

After Creating Models
-------------------------
```bash
python manage.py db migrate
```

Documenting Code
-----------------
```bash
sphinx-quickstart
```

Production Setup
------------------

Heroku
```bash
heroku config:set FLASK_ENV=production
```

Dokku
```bash
dokku config:set FLASK_ENV=production
```

Dokku Specific Instructions
-----------------------------
Dokku uses root account to run processes thus it requires C_FORCE_ROOT.
```
dokku config:set C_FORCE_ROOT=True
```

sudo docker run -t --link rabbitmq_test-www:broker app/test-www:latest /bin/bash -c /start

sudo docker run -i -t --link rabbitmq_test-www:broker app/test-www:latest /bin/bash
