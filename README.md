# Flask Demo

## Virtual Environments

### Why needed?

Virtual environments make it easy to manage library dependencies across projects. So instead of installing a library system-wide it will only be installed in the project that needs it. [Here's](http://docs.python-guide.org/en/latest/dev/virtualenvs/) their website.

#### Setup (to be done in your idb project directory):

```
pip install virtualenv
virtualenv venv
source ./venv/bin/activate
```

Afterwards your prompt should look something like:
```
(venv)virgo$
```

Also create an app directory and a templates directory in that directory:
```
(venv)virgo$ mkdir app
(venv)virgo$ cd app
(venv)virgo$ mkdir templates
```

### Updating your requirements.txt
It's important to keep a file called requirements.txt to store all the libraries needed for your project to work. Doing this will make it easier to test on Travis and easier to deploy to a server.

This can be done by (and should probably be in your makefile):
```
python3 -m pip freeze > requirements.txt
```

# Flask
Flask is a [microframework](https://en.wikipedia.org/wiki/Microframework) to help us quickly build our web application. It includes [jinja](http://jinja.pocoo.org/docs/2.9/) for templating. Templating allows for easier creation of webpages by including programming logic. By default Jinja will look for your templates in the templates directory we created earlier.

Start by installing flask in our virtual environment:

```
(venv)virgo$ pip install flask
```

Now create a file called app.py in your app folder:
```
(venv)virgo$ cd app
(venv)virgo$ touch app.py
```

In your favorite text editor add the following to app.py:
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

if __name__ == "__main__":
    app.run()
```

# Test
You can run your web server locally by running the following:

```
(venv)virgo$ cd app
(venv)virgo$ python3 app.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now go to localhost:5000 in your browser to view your webpage!

# Database magic
We will be using SQLalchemy as an [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) for our [postgres](https://www.postgresql.org/) database. This allows us to treat the tables and rows as objects for easier use in our program. 
