from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def get_data():
    user = request.form["username"]
    pword = request.form["password"]
    return f"<h1>Name: {user}, Password: {pword}"


if __name__ == "__main__":
    app.run(debug=True)