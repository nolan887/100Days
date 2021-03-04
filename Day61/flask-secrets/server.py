from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key = "secretpassword"

class MyForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=("GET", "POST"))
def login():
    form = MyForm()
    if form.validate_on_submit():
        return render_template('/success')
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)