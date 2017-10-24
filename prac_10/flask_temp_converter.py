from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_screen():
    return "<h1>Temperature converter</h1> \ntype in f/temp in celsius to get temp in fahrenheit \n type in /c/temp in fahrenheit to get temp in celsius"


@app.route('/f/<celsius>')
def f(celsius):
    celsius = float(celsius)
    return "<h1>{} degrees Celsius is {} degrees Fahrenheit<h1>".format(celsius, cel_to_far(celsius))


@app.route('/c/<fahrenheit>')
def c(fahrenheit):
    fahrenheit = float(fahrenheit)
    return "<h1>{} degrees Fahrenheit is {} degrees Celsius<h1>".format(fahrenheit, far_to_cel(fahrenheit))


def cel_to_far(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return "{:.2f}".format(fahrenheit)


def far_to_cel(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return "{:.2f}".format(celsius)


if __name__ == "__main__":
    app.run()
