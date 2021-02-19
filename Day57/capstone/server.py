from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:num>')
def post(num):
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    blog_post = all_posts[num-1]
    return render_template("post.html", post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
