import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from urllib.parse import urlparse

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
    
    # Configure database
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        parsed_url = urlparse(database_url)
        app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{parsed_url.username}:{parsed_url.password}@{parsed_url.hostname}:{parsed_url.port}{parsed_url.path}?sslmode=require"
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    from app import routes
    app.register_blueprint(routes.bp)

    return app
    