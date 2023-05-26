import unittest
from unittest import TestCase
from app_texoit import db
from app_texoit import create_app
from app_texoit.utils import load_data
from app_texoit.movies.models import Movie


class TestDB(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        app.config['LIVESERVER_PORT'] = 8000,
        app.config['LIVESERVER_TIMEOUT'] = 10,
        self.app_context = app.app_context()
        self.app_context.push()
        return app
    def create_tables(self):
        with self.app.app_context():
            db.create_all()
            db.session.commit()
    def drop_tables(self):
        with self.app.app_context():
            db.drop_all()

    def setUp(self):
        self.app = self.create_app()
        self.client = self.app.test_client()
        self.create_tables()

    def tearDown(self):
        self.app_context.pop()
        self.drop_tables()

    def test_load_data(self):
        load_data(app=self.app)
        movie = Movie.query.filter_by(producers="Allan Carr").first()
        producer_check = movie.producers
        self.assertEqual(producer_check, "Allan Carr")


class TestApi(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        app.config['LIVESERVER_PORT'] = 8000,
        app.config['LIVESERVER_TIMEOUT'] = 10,
        # app.config['file_name'] = FILE_FOR_API
        self.app_context = app.app_context()
        self.app_context.push()
        return app
    def create_tables(self):
        with self.app.app_context():
            db.create_all()
            db.session.commit()

    def drop_tables(self):
        with self.app.app_context():
            db.drop_all()

    def setUp(self):
        self.app = self.create_app()
        self.client = self.app.test_client()
        self.create_tables()
        load_data(app=self.app)

    def tearDown(self):
        self.app_context.pop()
        self.drop_tables()

    def test_create_movie(self):
        year = "1987"
        title = "My born year"
        studios = "Mother Nature"
        producers = "Agustin Baltasar Maletti"
        winner = "yes"
        target_endpoint = f"/create_movie/year={year}/title={title}/studios={studios}/producers={producers}/winner={winner}"
        response = self.client.post(target_endpoint)
        movie = Movie.query.filter_by(title="My born year").first()
        producers_check = movie.producers
        self.assertEqual(producers_check, "Agustin Baltasar Maletti")
        self.assertEqual(response.status_code, 200)

    def test_read_movies(self):
        target_endpoint = f"/read_movies"
        response = self.client.get(target_endpoint)
        data = response.json
        self.assertEqual(len(data), 206)
        self.assertEqual(response.status_code, 200)

    def test_update_movie(self):
        year = 1900
        title = "updated title"
        studios = "update studio"
        producers = "updated producer"
        winner = "yes"
        id_target = 1
        target_endpoint = f"/update_movie/id={id_target}/year={year}/title={title}/studios={studios}/producers={producers}/winner={winner}"
        response = self.client.put(target_endpoint)
        movie = Movie.query.filter_by(id=id_target).first()
        self.assertEqual(movie.year, 1900)
        self.assertEqual(movie.title, "updated title")
        self.assertEqual(movie.studios, "update studio")
        self.assertEqual(movie.producers, "updated producer")
        self.assertEqual(movie.winner, "yes")
        self.assertEqual(response.status_code, 200)

    def test_patch_movie_year(self):
        year = 1900
        title = "updated title"
        id_target = 1
        target_endpoint = f"/patch_movie/id={id_target}/year={year}"
        response = self.client.patch(target_endpoint)
        movie = Movie.query.filter_by(id=id_target).first()
        self.assertEqual(movie.year, 1900)
        self.assertEqual(response.status_code, 200)

    def test_patch_movie_title(self):
        title = "updated title"
        id_target = 1
        target_endpoint = f"/patch_movie/id={id_target}/title={title}"
        response = self.client.patch(target_endpoint)
        movie = Movie.query.filter_by(id=id_target).first()
        self.assertEqual(movie.title, title)
        self.assertEqual(response.status_code, 200)

    def test_patch_movie_studios(self):
        studios = "updated studios"
        id_target = 1
        target_endpoint = f"/patch_movie/id={id_target}/studios={studios}"
        response = self.client.patch(target_endpoint)
        movie = Movie.query.filter_by(id=id_target).first()
        self.assertEqual(movie.studios, studios)
        self.assertEqual(response.status_code, 200)

    def test_patch_movie_producers(self):
        producers = "updated producers"
        id_target = 1
        target_endpoint = f"/patch_movie/id={id_target}/producers={producers}"
        response = self.client.patch(target_endpoint)
        movie = Movie.query.filter_by(id=id_target).first()
        self.assertEqual(movie.producers, producers)
        self.assertEqual(response.status_code, 200)

    def test_patch_movie_winner(self):
        winner = "yes"
        id_target = 1
        target_endpoint = f"/patch_movie/id={id_target}/winner={winner}"
        response = self.client.patch(target_endpoint)
        movie = Movie.query.filter_by(id=id_target).first()
        self.assertEqual(movie.winner, winner)
        self.assertEqual(response.status_code, 200)

    def test_delete_movie(self):
        id_target = 1
        target_endpoint = f"/delete_movie/id={id_target}"
        response = self.client.delete(target_endpoint)
        movie = Movie.query.filter_by(id=id_target).first()
        self.assertEqual(movie, None)
        self.assertEqual(response.status_code, 200)

    def test_main_task_max(self):
        """Test result for:
        'min': [{'previousWin': 2019,
                 'followingWin': <NA>,
                 'producer': 'Debra Hayward, Tim Bevan, Eric Fellner, and Tom Hooper',
                 'interval': 0}]
         'max': [{'previousWin': 1984,
            'followingWin': 1990,
            'producer': 'Bo Derek',
            'interval': 6}]}
        """
        target_endpoint = f"/main_task"
        response = self.client.get(target_endpoint)
        data = response.json
        producer = data["max"][0]["producer"]
        interval = data["max"][0]["interval"]
        previous_win = data["max"][0]["previousWin"]
        following_win = data["max"][0]["followingWin"]

        self.assertEqual(producer, 'Bo Derek')
        self.assertEqual(interval, 6)
        self.assertEqual(previous_win, 1984)
        self.assertEqual(following_win, 1990)

    def test_main_task_min(self):
        """Test result for:
        'min': [{'previousWin': 2019,
                 'followingWin': <NA>,
                 'producer': 'Debra Hayward, Tim Bevan, Eric Fellner, and Tom Hooper',
                 'interval': 0}]
         'max': [{'previousWin': 1984,
            'followingWin': 1990,
            'producer': 'Bo Derek',
            'interval': 6}]}
        """
        target_endpoint = f"/main_task"
        response = self.client.get(target_endpoint)
        data = response.json
        producer_list = [data["min"][i]["producer"] for i in range(len(data["min"]))]
        self.assertIn('Debra Hayward, Tim Bevan, Eric Fellner, and Tom Hooper', producer_list)
