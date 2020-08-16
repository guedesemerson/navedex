# Description

In this sample application, you will execute aapi using Django and Django Rest Framework, with standard best practices and respecting the rules.

# Navedex Api

This app contains an opinionated set of endpoints for web serving:

## Steps

### Execute web service
You can get started building this application locally, but you can either run the application in web using the heroku link host web (http://navedexapi.herokuapp.com).

### Building Locally
* Python >= 3.6
* Install [Python](https://www.python.org/downloads/)

### Create and activate your virtuanenv
```bash
virtualenv -p python3 virtualEnv 
source virtualEnv/bin/activate
```

### Running Django applications: You can download the project dependencies with:

```bash
pip install -r requirements.txt
python manage.py migrate
```

### To run your application locally:

```bash
python manage.py runserver
```

### Your application will be running at `http://127.0.0.1:8000` with a doc api in the same page. 

