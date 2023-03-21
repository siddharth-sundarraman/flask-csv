import io
import pandas as pd
import unittest
from app import create_app, db
from sqlalchemy import text

class ApiTest(unittest.TestCase):
    
    # Create app and dummy CSV data
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
        self.csv_data = 'name,score,grade\nSiddharth,95,A\nAshish,93,A\nRobert,82,B-\n'
    
    # Test for post request response
    def test_post_csv_data(self):

        # Convert CSV data to give file-like object and send post request
        csv_data = self.csv_data.encode('utf-8')
        csv_file = io.BytesIO(csv_data)
        response = self.client.post('/api/file-import', content_type='multipart/form-data', data={
                                    'files': (csv_file, 'test.csv'),
                                    'create_usr_id': 'ashish',
                                    'schema': 'public',
                                })

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

    # Test for inserting csv data into database
    def test_insert_data(self):

        # Convert CSV data to a Pandas DataFrame
        df = pd.read_csv(io.StringIO(self.csv_data))

        # Insert data into the database using DataFrame.to_sql method
        table_name = 'test_table'
        df.to_sql(table_name, db.engine, if_exists='fail', index=False)
        db.session.commit()

        # Query data from the database and check that it matches the expected data
        query = text("SELECT * FROM test_table")
        result = db.session.execute(query).fetchall()

        expected_data = [
            ('Siddharth',95,'A'),
            ('Ashish',93,'A'),
            ('Robert',82,'B-'),
        ]

        self.assertEqual(result, expected_data)

    # Drop test table
    def tearDown(self):
        drop_table = text('DROP TABLE IF EXISTS test_table')
        db.session.execute(drop_table)
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
       

