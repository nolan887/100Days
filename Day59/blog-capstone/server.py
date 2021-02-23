from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    requested_post = posts[index - 1]
    return render_template("post.html", post=requested_post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)