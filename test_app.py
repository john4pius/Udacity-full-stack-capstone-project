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
