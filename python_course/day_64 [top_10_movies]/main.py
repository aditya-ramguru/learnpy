from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


all_movie_id = {}
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my-movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)
APIKEY = '7575b562bc49ab6cf76fc6dd10326118'


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(255), nullable=True)
    img_url = db.Column(db.String(255), nullable=False)


db.create_all()
# new_movie = Movie(title='Phone Booth',
#                   year=2002,
#                   description="Publicist Stuart Shepard finds himself trapped in a phone pinned down by an "
#                               "extortionist's sniper rifle. Unable to leave or receive outside help, "
#                               "Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#                   rating=7.3,
#                   ranking=10,
#                   review="My favourite character was the caller",
#                   img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")
#
# db.session.add(new_movie)
# db.session.commit()


class Editform(FlaskForm):
    rating = StringField(label='Your Rating out of 10 e.g. 8.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


class Addform(FlaskForm):
    movie_name = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()
    for movie in all_movies:
        movie.ranking = len(all_movies) - all_movies.index(movie)
    return render_template("index.html", allmovies=all_movies)


@app.route("/edit/<int:m_id>", methods=['GET','POST'])
def edit(m_id):
    edit_form = Editform()
    movie_to_update = Movie.query.get(m_id)
    if edit_form.validate_on_submit():
        movie_to_update.rating = edit_form.rating.data
        movie_to_update.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=edit_form, movie=movie_to_update)


@app.route('/delete/<int:m_id>')
def delete(m_id):
    movie_to_delete = Movie.query.get(m_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = Addform()
    if add_form.validate_on_submit():
        movie_title = add_form.movie_name.data

        SEARCH_API_ENDPOINT = 'https://api.themoviedb.org/3/search/movie'
        search_parameters = {
            'api_key': APIKEY,
            'query': f'{movie_title}'
        }
        response = requests.get(url=SEARCH_API_ENDPOINT, params=search_parameters)
        response.raise_for_status()
        data = response.json()['results']
        all_movie_data = {data[i]['original_title']: [data[i]['release_date'], data[i]['id'], data[i]['overview']] for i in range(len(data) - 1)}
        return render_template('select.html', allmovie=all_movie_data)
    return render_template('add.html', form=add_form)


@app.route('/selected/<name>/<year>/<m_id>/<overview>')
def from_selected(name, year, m_id, overview):
    TMDB_API_ENDPOINT = f'https://api.themoviedb.org/3/movie/{m_id}'
    TMDB_parameters = {
        'api_key': APIKEY,
    }
    response2 = requests.get(url=TMDB_API_ENDPOINT, params=TMDB_parameters)
    response2.raise_for_status()
    movie_data = response2.json()
    poster_path=f'https://image.tmdb.org/t/p/w500/{movie_data["poster_path"]}'
    selected_movie = Movie(title=name, year=year, description=overview, img_url=poster_path, rating=None, review=None,
                           ranking=None)
    db.session.add(selected_movie)
    db.session.commit()
    movie = Movie.query.filter_by(title=name).first()
    return redirect(url_for('edit', m_id=movie.id))


if __name__ == '__main__':
    app.run(debug=True)
