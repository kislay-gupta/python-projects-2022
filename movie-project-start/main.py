from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

API_KEY = ' GET YOUR API KEY FROM themoviedb.org'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return f'<Movie {self.title}>'





class AddMovie(FlaskForm):
    add_movie = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class MovieRating(FlaskForm):
    rating = StringField('Your Rating Out of 10. e.g 7.5', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Done')





@app.route("/")
def home():
    db.create_all()

    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        parameter = {
            'api_key': API_KEY,
            'query': form.add_movie.data
        }
        response = requests.get(url="https://api.themoviedb.org/3/search/movie", params=parameter)
        data = response.json()['results']

        return render_template('select.html', options=data)

    return render_template('add.html', form=form)


@app.route('/todb', methods=['GET', 'POST'])
def addtodb():
    movie_id = request.args.get("id")
    parameter = {
        'api_key': API_KEY
    }
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?', params=parameter)
    data = response.json()
    print(data['release_date'])
    new_movie = Movie(
        title=data['original_title'],
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
        year=data['release_date'].split("-")[0],
        description=data['overview']
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit', id=new_movie.id))


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = MovieRating()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie)


@app.route("/delete", methods=['GET', 'POST'])
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
