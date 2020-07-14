import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie, db_drop_and_create, insert_seed_records

from datetime import date

casting_assistant_auth_header = {
    "Authorization": "Bearer " + os.environ['CASTING_ASSISTANT_TOKEN']
}

casting_director_auth_header = {
    "Authorization": "Bearer " + os.environ['CASTING_DIRECTOR_TOKEN'] 
}

executive_producer_auth_header = {
    "Authorization": "Bearer " + os.environ['EXECUTIVE_PRODUCER_TOKEN']
}


class BoxofficeTestCase(unittest.TestCase):

    def setUp(self):

        self.app = create_app()
        self.client = self.app.test_client

        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', "agency_test")

        setup_db(self.app, self.database_path)
        db_drop_and_create()

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()



    ''' get movies '''

    def test_get_movies(self):
        response = self.client().get("/movies", headers=casting_assistant_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(len(data["movies"]), 1)

    def test_get_movies_not_authorized(self):
        response = self.client().get("/movies")

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)


    ''' create movies '''

    def test_create_movie(self):
        new_movie = {
            "title": "Titanic",
            "release_date": date.today()
        }

        response = self.client().post("/movies", json=new_movie,
                                      headers=executive_producer_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_create_movie_not_authorized(self):
        new_movie = {
            "title": "Titanic",
            "release_date": date.today()
        }

        response = self.client().post("/movies", json=new_movie,
                                      headers=casting_assistant_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertFalse(data["success"])


    ''' update movies '''

    def test_update_movie(self):
        update_movie = {"title": "Avatar"}
        response = self.client().patch("/movies/1", json=update_movie,
                                       headers=casting_director_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_update_movie_unauthorized(self):
        update_movie = {"title": "Avatar"}
        response = self.client().patch("/movies/1", json=update_movie,
                                       headers=casting_assistant_auth_header)

        
        data = json.loads(response.data)
        print(data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(data["success"])

    
    ''' delete movie '''

    def test_delete_movie(self):
        response = self.client().delete("/movies/1", headers=executive_producer_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_delete_movie_unauthorized(self):
        response = self.client().delete("/movies/1", headers=casting_assistant_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(data["success"])

    def test_delete_movie_not_found(self):
        response = self.client().delete(
            "/movies/5000", headers=executive_producer_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
