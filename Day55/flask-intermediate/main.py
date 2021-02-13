from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def bye():
    return "Bye!"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, your favorite number is {number}!"

if __name__ == "__main__":
    app.run(debug=True)
