from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

def get_age(name):
    endpoint = "https://api.agify.io?name=" + name
    response = requests.get(endpoint).json()
    guessed_age = response["age"]
    return guessed_age

def get_gender(name):
    endpoint = "https://api.genderize.io?name=" + name
    response = requests.get(endpoint).json()
    guessed_gender = response["gender"]
    return guessed_gender

def get_probability(name):
    endpoint = "https://api.genderize.io?name=" + name
    response = requests.get(endpoint).json()
    gender_probability = float(response["probability"]) * 100
    return gender_probability

@app.route('/')
def home():
    random_number = random.randint(1,10)
    year = datetime.now().year
    return render_template('index.html', num=random_number, current_yr=year)

@app.route('/guess/<string:name>')
def guess(name):
    age = get_age(name)
    gender = get_gender(name)
    probability = get_probability(name)
    return f"<h1>Hello, {name.title()}!" \
           f"<br>I'm {probability}% sure you are a {gender}" \
           f"<br>Age guess: {age}"

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)