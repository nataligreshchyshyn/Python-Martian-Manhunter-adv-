from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def greetings():
    return render_template("greet.html")


@app.route('/calc', methods=['POST', 'GET'])
def calculator():
    return f'This is a simple calculator'


@app.route('/calc/<int:x>/<int:y>/div')
def div(x, y):
    return render_template('calculator.html', x=x, y=y,
                           result=f'{x} / {y} = {x / y}')


@app.route('/calc/<int:x>/<int:y>/sum')
def suma(x, y):
    return render_template('calculator.html', x=x, y=y,
                           result=f'{x} + {y} = {x + y}')


@app.route('/calc/<int:x>/<int:y>/dif')
def dif(x, y):
    return render_template('calculator.html', x=x, y=y,
                           result=f'{x} - {y} = {x - y}')


@app.route('/calc/<int:x>/<int:y>/mult')
def mult(x, y):
    return render_template('calculator.html', x=x, y=y,
                           result=f'{x} * {y} = {x * y}')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
