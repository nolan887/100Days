from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key = "secretpassword"

class MyForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=("GET", "POST"))
def login():
    form = MyForm()
    if form.validate_on_submit():
        return render_template('success.html')
    return render_template("login.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)