import logging
from colorlog import ColoredFormatter
import sqlite3
import pandas as pd
from app_texoit.settings import DATA_FILE
from app_texoit.movies.models import Movie
from app_texoit import db
import numpy as np

def setup_logger():
    # PARENT_DIR = Path(base_path)
    # LOG_DIR = PARENT_DIR.joinpath('LOGS')
    """
    Log levels:
    critical 50, error 40, warning 30, info 20, debug 10, notset 0
    """

    """Return a logger with a default ColoredFormatter."""
    formatter = ColoredFormatter("%(log_color)s%(levelname)-8s%(reset)s %(bold_blue)s%(message)s",
                                 datefmt=None, reset=True, log_colors={
            'DEBUG': 'cyan',
            'INFO': 'bold_green',
            'WARNING': 'red',
            'ERROR': 'bold_red',
            'CRITICAL': 'bold_red',
            'DATA': 'bold_purple'
        })
    logging.addLevelName(19, 'DATA')
    logger = logging.getLogger()
    return logger
logger = setup_logger()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


def create_tables(app):
    with app.app_context():
        db.create_all()
        db.session.commit()

def drop_tables(app):
    with app.app_context():
        db.drop_all()

def load_data(app):
    data = pd.read_csv(DATA_FILE, sep=";")

    for index, row in data.iterrows():
        row = row.to_dict()
        year = int(row["year"])
        title = row["title"]
        studios = row["studios"]
        producers = row["producers"]
        winner = row["winner"]
        movie = Movie(
            year=year,
            title=title,
            studios=studios,
            producers=producers,
            winner=winner,)
        with app.app_context():
            db.session.add(movie)
            db.session.commit()


def get_intervals_max_and_min(df_movies):
    dfs_producers = []
    df_movies_sel_intervals = df_movies[df_movies.winner =='yes']

    init_flag = 0
    for producers in df_movies_sel_intervals.producers.unique():
        df_producers = df_movies_sel_intervals[df_movies_sel_intervals.producers == producers]
        df_producers.sort_values("year").reset_index()
        if df_producers.shape[0] > 1:
            for idx, row in df_producers.iterrows():
                year = row["year"]
                title = row["title"]
                producers =  row["producers"]
                winner = row["winner"]
                if not init_flag:
                    previous_win = year
                    init_flag = 1
                else:
                    following_win = year
                    interval = following_win - previous_win
                    data = {"previousWin": previous_win, "followingWin": following_win, "producer": producers, "interval":interval}
                    dfs_producers.append(data)
                    previous_win = following_win
        else:
            for idx, row in df_producers.iterrows():
                year = row["year"]
                title = row["title"]
                producers =  row["producers"]
                winner = row["winner"]
                data = {"previousWin": year , "followingWin": np.nan, "producer": producers, "interval": 0, }
            dfs_producers.append(data)
    df_producers_interval = pd.DataFrame(dfs_producers)
    df_producers_interval.followingWin = df_producers_interval.followingWin.astype('Int64')
    min_interval = df_producers_interval.interval.min()
    max_interval = df_producers_interval.interval.max()
    df_producers_interval_min = df_producers_interval[df_producers_interval.interval == min_interval]
    df_producers_interval_max = df_producers_interval[df_producers_interval.interval == max_interval]
    data_output = {"min": df_producers_interval_min.to_dict('records'), "max": df_producers_interval_max.to_dict('records')}
    return data_output



#------------#------------#------------#------------#------------#------------#------------#------------#------------#------------
# import json
# import jaydebeapi
# from app_texoit.settings import DB_H2_PATH
# from app_texoit.settings import DB_SQLITE3