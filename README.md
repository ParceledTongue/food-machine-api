You will first need [virtualenv](https://pypi.python.org/pypi/virtualenv). 
Then, in the root project folder, run `virtualenv flask`.
Once this is done, do `flask/bin'pip install flask.

Then do all of the following (though it is not all necessary now or maybe ever).

```
$ flask/bin/pip install flask
$ flask/bin/pip install flask-login
$ flask/bin/pip install flask-openid
$ flask/bin/pip install flask-mail
$ flask/bin/pip install flask-sqlalchemy
$ flask/bin/pip install sqlalchemy-migrate
$ flask/bin/pip install flask-whooshalchemy
$ flask/bin/pip install flask-wtf
$ flask/bin/pip install flask-babel
$ flask/bin/pip install guess_language
$ flask/bin/pip install flipflop
$ flask/bin/pip install coverage
```

Finally, do `./db_migrate` followed by `./db_create` to create the database.

You can see the complete database model in action by interfacing with it
via the Python shell `/flask/bin/python` and SQLAlchemy calls.

You can access the GET views via your web browser. You can do more complex calls
with curl, e.g. to add sliced apple: 

`curl -i -H "Content-Type: application/json" -X POST -d '{"name":"apple (sliced)", "calories":50,"category":3,"unit":"apple"}' http://localhost:5000/foodmachine/api/ingredients`
