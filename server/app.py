from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('<h1>Python Operations with Flask Routing and Views</h1>')

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  
    return parameter  

@app.route('/count/<int:parameter>')
def count(parameter):
    return '<br>'.join(map(str, range(parameter)))

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mul':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Cannot divide by zero!'
        result = num1 / num2
    elif operation == 'mod':
        result = num1 % num2
    else:
        return 'Invalid operation!'
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
