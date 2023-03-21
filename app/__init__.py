from flask import Flask
from .api.routes import api_bp
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

# Initialize app
def create_app():
    app = Flask(__name__)

    # Initialize db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)

    migrate.init_app(app, db)


    # Register api blueprint
    app.register_blueprint(api_bp)

    return app

