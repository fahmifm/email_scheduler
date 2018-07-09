from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config
import os

config_name = os.getenv('FLASK_ENV') if os.getenv('FLASK_ENV') else 'development'

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(app_config[config_name])
db.init_app(app)

migrate = Migrate(app, db)

# register endpoint
from route import data as data_blueprint
app.register_blueprint(data_blueprint, url_prefix='/api')
