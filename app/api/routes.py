from flask import Blueprint, request
from flask_restful import Api, Resource
import pandas as pd
from datetime import datetime


# Initialize api blueprint
api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

class FileImport(Resource):
    def post(self):
        from .. import db
        try:

            # Read request form
            file = request.files['files']
            user_id = request.form['create_usr_id']
            schema = request.form['schema']

            # Read CSV as dataframe
            csv_data = pd.read_csv(file)

            # Set name for table using specified user and schema
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            table_name = f'{schema}.table_{user_id}_{timestamp}'

            # Save dataframe into new table
            csv_data.to_sql(table_name, con=db.engine, if_exists='fail', index=False)
            db.session.commit()

            return {'success':f'CSV has been uploaded and saved into new table : {table_name}'}, 200
    
        except Exception as e:
            return {'error': str(e)}, 500
    
    def get(self):
        return {'message':'upload csv and save to database'}
    
        
api.add_resource(FileImport, '/file-import')