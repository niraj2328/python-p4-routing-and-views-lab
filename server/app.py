#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param: str):
    print(param)
    return param

@app.route('/count/<int:num>')
def count(num: int):
    nums = range(num)
    string = '\n'.join(map(str, nums))
    return string

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1: int, operation: str, num2: int):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation'

if __name__ == '__main__':
    app.run(port=5555, debug=True)