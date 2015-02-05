Token Based Authentication with Flask-Security
##############################################

:date: 2015-01-15
:modified: 2015-02-03
:category: tutorial
:slug: token-auth-with-flask-security
:tags: how-to, python, learning
:author: Mandar Vaze

.. contents::
..
   1  Intro
   2  Define User and Roles
   3  Configurations
   4  API Endpoint
   5  Lets Test
   6  Another Configuration
   7  Get the Token


Intro
-----

I'm working on a Flask based API server (why Flask, why not xyz - is a topic for another discussion, but FWIW I am considering Django)

As you know, Flask is a micro framework - that means a lot of "features" that are built-in into other frameworks aren't part of Flask. But there are several third party Flask extension. Flask-Security is one of them (Flask-Restless is another one I'll be using)

Unfortunately, documentation for Flask-Security isn't up to the mark (at least as of this writing). I know this could be flame-bait, but it is not. Sometimes users need more sample code along with documentation, which seems to be missing here, and I am not alone. Just looking at the SO and other places people are "stuck" - lack of tutorials is evident.

I went thru the documentation, SO links, Google Searches, Flask-Security code walk thru, debugging that code, looking at the Flask-Security test cases. All of it finally was worth it, because I was able to get Token based Authentication to work.

Define User and Roles
---------------------

Basic code that defines the ``User`` and ``Role`` classes, initializes Flask-Security extension.
This is not different from what is available in the documentation (Except may be additional attributes for ``User`` class)

.. code-block:: python

	# A base model for other database tables to inherit
	class Base(db.Model):
	    __abstract__ = True
	    id = db.Column(db.Integer, primary_key=True)
	    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
	    modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
	                            onupdate=db.func.current_timestamp())


	roles_users = db.Table('roles_users',
	                       db.Column('user_id', db.Integer(),
	                                 db.ForeignKey('auth_user.id')),
	                       db.Column('role_id', db.Integer(),
	                                 db.ForeignKey('auth_role.id')))


	class Role(Base, RoleMixin):
	    __tablename__ = 'auth_role'
	    name = db.Column(db.String(80), nullable=False, unique=True)
	    description = db.Column(db.String(255))

	    def __init__(self, name):
	        self.name = name

	    def __repr__(self):
	        return '<Role %r>' % self.name


	class User(Base, UserMixin):
	    __tablename__ = 'auth_user'
	    email = db.Column(db.String(255), nullable=False, unique=True)
	    password = db.Column(db.String(255), nullable=False)
	    first_name = db.Column(db.String(255))
	    last_name = db.Column(db.String(255))
	    active = db.Column(db.Boolean())
	    confirmed_at = db.Column(db.DateTime())
	    last_login_at = db.Column(db.DateTime())
	    current_login_at = db.Column(db.DateTime())
	    # Why 45 characters for IP Address ?
	    # See http://stackoverflow.com/questions/166132/maximum-length-of-the-textual-representation-of-an-ipv6-address/166157#166157
	    last_login_ip = db.Column(db.String(45))
	    current_login_ip = db.Column(db.String(45))
	    login_count = db.Column(db.Integer)
	    roles = db.relationship('Role', secondary=roles_users,
	                            backref=db.backref('users', lazy='dynamic'))

	    def __repr__(self):
	        return '<User %r>' % self.email


	# Setup Flask-Security
	user_datastore = SQLAlchemyUserDatastore(db, User, Role)
	security = Security(app, user_datastore)


	# Create a user to test with
	@app.before_first_request
	def create_user():
	    db.create_all()
	    if not User.query.first():
	        user_datastore.create_user(email='test@example.com', password='test123')
	        db.session.commit()

Configurations
--------------

In the ``config.py`` I have following flask security configurations (for now - more will come)

.. code-block:: python

    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_SALT = 'something_super_secret_change_in_production'


API Endpoint
------------

Add a dummy API endpoint like this :

.. code-block:: python

	from flask_security import auth_token_required
	from flask import jsonify


	@app.route('/dummy-api/', methods=['GET'])
	@auth_token_required
	def dummyAPI():
	    ret_dict = {
	        "Key1": "Value1",
	        "Key2": "value2"
	    }
	    return jsonify(items=ret_dict)


Lets Test
---------

Now all the pieces are set. Lets test.

Lets try whether authentication itself works.

First change  the ``@auth_token_required`` decorator to ``@http_auth_required``

Now you can now access the URL ``127.0.0.1:5001/dummy-api/`` via the browser.
You will see a pop up dialog that asks for the username and password

Enter the email as username and password we created earlier with ``create_user``

If you dismiss without username password - you should see message starting with "Unauthorized"
If you entered the email and password correctly - you should see the dummy JSON data we returned in the browser page.

One other option is to use a program like curl or http (I prefer this. ``pip install httpie``) e.g.

.. code-block:: bash

	$ http 127.0.0.1:5001/dummy-api/
	HTTP/1.0 401 UNAUTHORIZED
	Content-Length: 271
	Content-Type: text/html; charset=utf-8
	Date: Wed, 14 Jan 2015 07:56:55 GMT
	Server: Werkzeug/0.9.6 Python/3.4.0
	Set-Cookie: session=eyJfaWQiOiIwZTMxMDBkNmMwNmY0MmQyNmU3MDBhYTZkMzUxZmM4OSJ9.B5eyxw.074cU7O6pJha_qomfuUOG2CvZNg; HttpOnly; Path=/
	WWW-Authenticate: Basic realm="Login Required"

	<h1>Unauthorized</h1>
	    <p>The server could not verify that you are authorized to access the URL
	    requested. You either supplied the wrong credentials (e.g. a bad password),
	    or your browser doesn't understand how to supply the credentials required.</p>

Now provide the authentication details, and see the expected response :

.. code-block:: bash

	$ http -a test@example.com:test123 127.0.0.1:5001/dummy-api/
	HTTP/1.0 200 OK
	Content-Length: 63
	Content-Type: application/json
	Date: Wed, 14 Jan 2015 08:03:50 GMT
	Server: Werkzeug/0.9.6 Python/3.4.0
	Set-Cookie: session=eyJfaWQiOiIwZTMxMDBkNmMwNmY0MmQyNmU3MDBhYTZkMzUxZmM4OSJ9.B5e0Zg.9-MG7d6XQ3zFnsNEz6NR7LtEC6Y; HttpOnly; Path=/

	{
	    "items": {
	        "Key1": "Value1",
	        "Key2": "value2"
	    }
	}

So far so good. I was able to achieve this without too much trouble (Actually that is not true, but ..)

Lets move on to Token based Authentication. This is where things got a bit tricky (for me)
There seemed to be several people on SO with similar problems. (Hence this post - so that others in future can get some help)

First, before we forget, change the ``@http_auth_required`` decorator back to ``@auth_token_required``

Now to "get" the auth token. Per Flask Security documentation :

	Token based authentication is enabled by retrieving the user auth token by
	performing an HTTP POST with the authentication details as JSON data against
	the authentication endpoint. A successful call to this endpoint will return
	the user’s ID and their authentication token. This token can be used in
	subsequent requests to protected resources.

First of all - the documentation doesn't specify which *authentication endpoint* ?
Do I need to create one, or does Flask-Security provide me one by default ?

Turns out ``/login`` is that default provided by Flask-Security
(An older post on flask mailing list mentioned ``/auth``. May be it was, in 2012. Not anymore)

Testing ``http_auth`` was easy, also it was a ``GET`` request. Performing ``POST`` request isn't trivial.
At first I tried Postman client (Chrome Extension) - But it didn't work.

Then on SO - I came across `this <http://stackoverflow.com/questions/24186694/combining-flask-restless-flask-security-and-regular-python-requests>`_ post. While that person went with `Flask-JWT` - I didn't need to. It gave me an idea of using `requests` for the `POST` call.

Another Configuration
---------------------

But before all is well - we need one entry in config.py as follows :

.. code-block:: python

    # Without this get_auth_token via POST request w/ JSON data does not work
    # You keep getting "CSRF token missing" error
    WTF_CSRF_ENABLED = False

Get the Token
-------------

I did the following in ipython console - but one can very well convert this to a stand alone script, if needed.

.. code-block:: python

	In [20]: import requests

	In [21]: import json

	In [22]: r = requests.post('http://127.0.0.1:5001/login', data=json.dumps({'email':'test@example.com', 'password':'test123'}), headers={'content-type': 'application/json'})

	In [23]: r.json()
	Out[23]:
	{'meta': {'code': 200},
	 'response': {'user': {'authentication_token': 'WyIxIiwiY2UwZWY0MDFjYTA3MmJlODcyODkzYjYxOGQzZjk4YzUiXQ.B5e5Sg.qcsDcaMgiRqx21YTC0OwwnihINM',
	   'id': '1'}}}

Now I can use this token with http as follows :

.. code-block:: shell

	$ http 127.0.0.1:5001/dummy-api/ Authentication-Token:WyIxIiwiY2UwZWY0MDFjYTA3MmJlODcyODkzYjYxOGQzZjk4YzUiXQ.B5e5Sg.qcsDcaMgiRqx21YTC0OwwnihINM
	HTTP/1.0 200 OK
	Content-Length: 63
	Content-Type: application/json
	Date: Wed, 14 Jan 2015 08:26:48 GMT
	Server: Werkzeug/0.9.6 Python/3.4.0
	Set-Cookie: session=eyJfaWQiOiIwZTMxMDBkNmMwNmY0MmQyNmU3MDBhYTZkMzUxZmM4OSJ9.B5e5yA.Oog7nYYA6zSvWjyS7mVUUropKj8; HttpOnly; Path=/

	{
	    "items": {
	        "Key1": "Value1",
	        "Key2": "value2"
	    }
	}

Success !!!

*Note: I'm yet to separate the Flask-Security related code into a separate file. When I did that hell broke loose. For now I have everything under myapp/__init__.py file. May be I'll cover that in another blog post*
