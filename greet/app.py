# In the greet folder, Make a simple Flask app that responds to these routes with simple text messages:

from flask import Flask, request
app = Flask(__name__)

# /welcome
# Returns “welcome”

@app.route('/welcome')
def welcome_pg():
    html = '<h1>Welcome!</h1>'
    return html

# /welcome/home
# Returns “welcome home”

@app.route('/welcome/home')
def welcome_home():
    html = '<h1>Welcome Home!</h1>'
    return html

# /welcome/back
# Return “welcome back”
@app.route('/welcome/back')
def welcome_back():
    html = '<h1>Welcome back</h1>'
    return html
# Once you’ve finished this, run the tests for it: