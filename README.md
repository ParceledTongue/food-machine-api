Food Machine
============


Using the API
-------------

This REST API is hosted at `https://food-machine-api.herokuapp.com`, and this is
the base URL for all requests. Each item returned from the database includes a
URI where future requests can be sent to retrieve, modify, or delete that
item's information.

`GET` requests are used to retrieve item information (in JSON format) from the
database. They can be used to get specific items via URI, or they can be used to
get a list of all items of a particular type, e.g. 
`https://food-machine-api.herokuapp.com/ingredients` to retrieve a full list of
ingredients.

`POST` requests are used to add items to the database. A request returns the
JSON of the added item. It must contain the JSON representation of the object to
be added. An example `curl` command:

```
curl -H "Content-Type: application/json" -X POST -d '{"name":"apple (sliced)", "calories":50, "category":3,"unit":0}' https://food-machine-api.herokuapp.com/ingredients
```

`PUT` requests are used to update item information in the database. They can
contain full or partial information for the object (and the old values are used
for unspecified fields). For example, say the sliced apple ingredient above has
the URI `http://food-machine-api.herokuapp.com/ingredients/1`. The following
`curl` command updates the number of calories to 70:

```
curl -H "Content-Type: application/json" -X PUT -d '{"calories":70}' https://food-machine-api.herokuapp.com/ingredients/1
```

`DELETE` requests are probably about as self-explanatory as `GET` requests. A
DELETE request returns the JSON of the deleted item. To delete our sliced apple:

```
curl -X DELETE https://food-machine-api.herokuapp.com/ingredients/1
```


JSON Structure
--------------

Notes:
- All names must be unique
- All returned JSON objects will include an extra `"uri"` field by which to 
  reference the object.

```
{
  "name": STRING(64),
  "calories": INT,
  "category": INT,
  "unit": INT
}
```


Running Locally
---------------

You will first need [virtualenv](https://pypi.python.org/pypi/virtualenv). 
Then, in the root project folder, run `virtualenv flask`.
Once this is done, do `flask/bin/pip install flask`.

Then do all of the following (though not all of it is necessary now or maybe
ever).

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

Do `./db_create` followed by `./db_migrate` to set up the database.

Finally, run  with `./run.py`. It will be hosted on `localhost`.

You can see the complete database model in action by interfacing with it
via the Python shell `/flask/bin/python` and SQLAlchemy calls.
