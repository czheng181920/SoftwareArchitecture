# SoftwareArchitecture

Software Architecture Assignment 1(Team 3)

# Setup

run this to set up the database (have to change python3 to python if that is what you are using)

`python3 db.py`

# Running CLI

You can run the CLI by typing these commands in the terminal.

Run the cli.py file and follow commands as shown.

`python3 cli.py`

# Running Frontend(Flask)

First cd into the Presentation Layer
`cd Presentation_Layer`

run python virtual environment
`python3 -m venv .venv `
`. .venv/bin/activate`

Then, make sure you have the required packages downloaded

If you don't, then do this:
`pip install -r requirements.txt`

To run the frontend:
`flask run`
or if that doesn't work, the following will always run the server
`python app.py` 

Then you should get something like this:

- Debug mode: off
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
- Running on http://127.0.0.1:5000
  Press CTRL+C to quit

Copy and paste the http link to your web browser to see web app

# Running either the business layer or data layer server
First cd into the correct folder
`cd`

run python virtual environment
`python3 -m venv .venv `
`. .venv/bin/activate`

Then, make sure you have the required packages downloaded

If you don't, then do this:
`pip install -r requirements.txt`

To run the frontend:
`flask run` 
or if that doesn't work, the following will always run the server
`python app.py` 

# Updating the requirements.txt 
If you add a package to a server, you can update the dependencies by doing this:
`pip freeze > requirements.txt`