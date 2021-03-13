from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

movie_API = "dfcf38f0756fec961c14002048b0e1bf"
movie_search_URL = f"https://api.themoviedb.org/3/search/movie?api_key={movie_API}&query="
movie_known_URL = f"https://api.themoviedb.org/3/movie"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# SQLAlchemy
# Creates the new database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-shelf.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Creates the new table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, primary_key=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, primary_key=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
db.create_all()

# WTForm
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_movie_url = movie_search_URL + request.form["title"]
        response = requests.get(url=new_movie_url)
        response.raise_for_status()
        data = response.json()["results"]
        return render_template("select.html", movie_search=data)
    form = AddMovieForm()
    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    print(movie_api_id)
    if movie_api_id:
        movie_api_url = f"{movie_known_URL}/{movie_api_id}?api_key={movie_API}"
        print(movie_api_url)
        response = requests.get(url=movie_api_url)
        data = response.json()
        print(data[""])
    # new_movie = Movie(
    #     title = request.form["title"],
    #     year = "1969",
    #     description = "fake credentials",
    #     rating = "6.9",
    #     ranking = "5",
    #     review = "bad",
    #     img_url = ""
    # )


    # db.session.add(new_movie)
    # db.session.commit()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
