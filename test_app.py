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


class MoviecastTestCase(unittest.TestCase):

    def setUp(self):

        self.app = create_app()
        self.client = self.app.test_client

        ''' self.database_path = "postgres://{}/{}".format(
            'localhost:5432', "moviecast") '''
            
        self.database_path = 'postgres://demorole1:password1@localhost:5432/moviecast'


        setup_db(self.app, self.database_path)
        db_drop_and_create()

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            
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
            "title": "Marshal",
            "release_date": date.today()
        }

        response = self.client().post("/movies", json=new_movie,
                                      headers=executive_producer_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_create_movie_not_authorized(self):
        new_movie = {
            "title": "Marshal",
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
        
        
    ''' get actors '''
    

    def test_get_actors(self):
        response = self.client().get("/actors", headers=casting_assistant_auth_header)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])
        self.assertEqual(len(data["actors"]), 1)

    def test_get_actors_not_authorized(self):
        response = self.client().get("/movies")

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    
    ''' create actor '''
    
    def test_create_actor(self):
        new_actor = {
            "name": "Steve",
            "age": 20,
            "gender": "Male"
        }
        response = self.client().post("/actors", json=new_actor,
                                      headers=casting_director_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_create_actor_not_authorized(self):
        new_actor = {
            "name": "Steve",
            "age": 20,
            "gender": "Male"
        }
        response = self.client().post("/actors", json=new_actor)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data["message"], "Authorization header is expected.")
        self.assertFalse(data["success"])

    
    ''' update actor '''
    

    def test_update_actor(self):
        updated_actor = {"name": "Bill"}
        response = self.client().patch("/actors/1", json=updated_actor,
                                       headers=casting_director_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_update_actor_unauthorized(self):
        updated_actor = {"name": "Bill"}
        response = self.client().patch(
            "/actors/1", json=updated_actor, headers=casting_assistant_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(data["success"])

    
    ''' delete actor '''
    
    def test_delete_actor(self):
        response = self.client().delete("/actors/1", headers=casting_director_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data["success"])

    def test_delete_actor_unauthorized(self):
        response = self.client().delete("/actors/1", headers=casting_assistant_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(data["success"])

    def test_delete_actor_not_found(self):
        response = self.client().delete("/actors/5000", headers=casting_director_auth_header)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)

'''
Make the tests conveniently executable.
From app directory, run 'python test_app.py' to start tests 
'''
if __name__ == "__main__":
    unittest.main()

