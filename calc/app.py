# Put your app in here.
# Calc
# Build a simple calculator with Flask, which uses URL query parameters to get the numbers to calculate with.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# Make a Flask app that responds to 4 different routes. Each route does a math operation with two numbers, a and b, which will be passed in as URL GET-style query parameters.

# /add
# Adds a and b and returns result as the body.
@app.route('/add')
def add_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1>{add(a,b)}</h1>"

# /sub
# Same, subtracting b from a.

@app.route('/sub')
def sub_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1>{sub(a,b)}</h1>"

# /mult
# Same, multiplying a and b.

@app.route('/mult')
def mult_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1>{mult(a,b)}</h1>"

# /div
# Same, dividing a by b.
@app.route('/div')
def div_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"<h1>{div(a,b)}</h1>"

# For example, a URL like http://localhost:5000/add?a=10&b=20 should return a string response of exactly 30.

# Write the routes for this but don’t hardcode the math operation in your route function directly. Instead, we’ve provided helper functions for this in the file operations.py:

@app.route('/math/<math_type>')
def do_math(math_type):
    a = int(request.args['a'])
    b = int(request.args['b'])
    math_methods = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div
    }
    sol = math_methods[f"{math_type}"](a,b)
    print(sol)
    return f"{sol}"