from flask import render_template, redirect, url_for, Blueprint, flash, session, current_app, abort
from app_texoit.utils import logger
from flask import jsonify
from app_texoit import db
from app_texoit.movies.models import Movie
from flask import make_response
from app_texoit.utils import get_intervals_max_and_min
import pandas as pd

movies = Blueprint('movies', __name__, template_folder='templates', static_folder='static', static_url_path='/movies/static')



@movies.route("/read_movies", methods=['GET'])
def read_movies():
    try:
        movies = Movie.query.all()
        all_data = []
        for movie in movies:
            data = {"year": movie.year, "title": movie.title, "studios": movie.studios, "producers": movie.producers, "winner": movie.winner}
            all_data.append(data)
        data = jsonify(all_data)
        response = make_response(data, 200)
        return response
    except Exception as error:
        data = jsonify([{"error": error}])
        response = make_response(data, 500)
        return response


@movies.route("/create_movie/year=<int:year>/title=<string:title>/studios=<string:studios>/producers=<string:producers>/winner=<string:winner>", methods=['POST'])
def create_movie(year: int, title: str, studios: str, producers: str, winner: str):
    try:
        logger.info(f"posted: {year} {title}, {studios}, {producers}, {winner}")
        movie = Movie(year=year, title=title, studios=studios, producers=producers, winner=winner)
        db.session.add(movie)
        db.session.commit()
        data = jsonify({"status": "movie inserted" })
        response = make_response(data,  200)
        return response
    except Exception as error:
        data = jsonify([{"error": error}])
        response = make_response(data, 500)
        return response


@movies.route("/update_movie/id=<int:id_number>/year=<int:year>/title=<string:title>/studios=<string:studios>/producers=<string:producers>/winner=<string:winner>", methods=['PUT'])
def update_movie(id_number, year: int, title: str, studios: str, producers: str, winner: str):
    try:
        movie = Movie.query.filter_by(id=id_number).first()

        movie.year = year
        movie.title = title
        movie.studios = studios
        movie.producers = producers
        movie.winner = winner
        db.session.commit()
        data_updated = {"id":id_number, "year":movie.year, "title": movie.title,
                       "studios": movie.studios, "producers": movie.producers,
                       "winner": movie.winner}
        data = jsonify({"status": "data updated", "data": data_updated})
        response = make_response(data, 200)
        return response
    except Exception as error:
        data = jsonify({"error": error})
        response = make_response(data, 500)
        return response

@movies.route("/patch_movie/id=<int:id_number>/year=<int:year>",   methods=['PATCH'])
@movies.route("/patch_movie/id=<int:id_number>/title=<string:title>",  methods=['PATCH'])
@movies.route("/patch_movie/id=<int:id_number>/studios=<string:studios>", methods=['PATCH'])
@movies.route("/patch_movie/id=<int:id_number>/producers=<string:producers>", methods=['PATCH'])
@movies.route("/patch_movie/id=<int:id_number>/winner=<string:winner>", methods=['PATCH'])
def patch_movie(id_number, year: int=None, title: str=None, studios: str=None, producers: str=None, winner: str=None):
    try:
        movie = Movie.query.filter_by(id=id_number).first()
        if year is not None:
            movie.year = year
        if title is not None:
            movie.title = title
        if studios is not None:
            movie.studios = studios
        if producers is not None:
            movie.producers = producers
        if winner is not None:
            movie.winner = winner
        db.session.commit()
        data_updated = {"id":id_number, "year":movie.year, "title": movie.title,
                       "studios": movie.studios, "producers": movie.producers,
                       "winner": movie.winner}
        data = jsonify({"status": "data partially updated", "data":data_updated})
        response = make_response(data, 200)
        return response
    except Exception as error:
        data = jsonify({"error": error})
        response = make_response(data, 500)


@movies.route("/delete_movie/id=<int:id_number>", methods=['DELETE'])
def delete_movie(id_number):
    try:
        Movie.query.filter_by(id=id_number).delete()
        data = jsonify([{"status": "movie deleted"}])
        response = make_response(data, 200)
        return response
    except Exception as error:
        data = jsonify({"error", error})
        response = make_response(data, 500)
        return response


@movies.route("/main_task", methods=["GET"])
def main_task():
    try:
        movies = Movie.query.all()
        movies = [{"id": d.id, "year": d.year, "title":d.title, "studios": d.studios,
                           "producers": d.producers, "winner": d.winner} for d in movies]
        df_movies = pd.DataFrame(movies)
        data = get_intervals_max_and_min(df_movies=df_movies)
        data = jsonify(data)
        response = make_response(data, 200)
        return response
    except Exception as error:
        data = jsonify({"error", error})
        response = make_response(data, 500)
        return response
