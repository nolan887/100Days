from flask import Flask

app = Flask(__name__)

# This circumvents the necessity to use terminal to run the server
if __name__ == "__main__":
    app.run()

@app.route('/')
def hello_world():
    return 'Hello, World!'





