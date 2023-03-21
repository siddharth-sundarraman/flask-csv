# Flask API for CSV file Uploads

This is a Flask API that allows you to upload a CSV file via POST request and save the contents into a new database table. It uses SQLalchemy for communication with database and pandas to read csv.

# Setup

Clone the repository with the following command:

```
git clone https://github.com/siddharth-sundarraman/flask-csv.git
```

Initialize virtual environment:

```
python -m venv venv
```
Activate virtual environment:

```
.\venv\Scripts\activate
```

Install required dependencies:

```
pip3 install -r requirements.txt
```

# Running the Flask App

```
python3 run.py
```

The server will run on http://localhost:5000

# Uploading CSV Files

To upload CSV files you can send POST requests using a tool like Postman or curl. 

The API endpoint for uploading is 
```
/api/file-import
```

The CSV will be saved in an sqlite database in the instance/project.db file

Sample post request format:

<img width="727" alt="postman" src="https://user-images.githubusercontent.com/111048443/226517431-06d0771f-9abb-4936-9a02-18d35a5cca33.png">

or curl command:

```curl
curl --location --request POST 'http://localhost:5000/api/file-import' \
--form 'files=@"/Users/sid/Downloads/grades.csv"' \
--form 'create_usr_id="sid"' \
--form 'schema="public"'
```


