from flask import Flask, render_template, request
import requests
import smtplib
import os

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

my_email = "pythoncraylie@gmail.com"
my_pass = os.environ.get("PYTHON_CRAYLIE_GMAIL_PW")

def send_form_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject: Web Contact Form!\n\n {name} has contacted you with the following information:"
                                f"\n{message}"
                                f"\nReturn contact information: phone - {phone}, e-mail: {email}".encode("utf-8"))


@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/form-entry', methods=["POST"])
def get_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    send_form_email(name, email, phone, message)
    return render_template('contact.html')

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