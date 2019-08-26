import os

from celery import Celery
from flask import Flask
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_login import LoginManager
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from webapp.utils import get_file_path


def create_app():
    app = Flask(__name__)
    # Get sql configuration file
    config_directory = "config"
    filepath = get_file_path(os.path.join(config_directory, "sqlconfig.py"))
    # Read configuration from python file
    app.config.from_pyfile(filepath)
    
    return app


app = create_app()
# Initialize app with database configurations
db = SQLAlchemy(app)
redis_client = FlaskRedis(app, strict=True)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
login_manager = LoginManager(app)
#login_manager.init_app(app)
admin = Admin(app, name='Product Mgmt', template_mode='bootstrap3')
admin.add_link(MenuLink(name='Main', category='', url="/"))

from webapp.auth.views import *
from webapp.product.views import *
db.create_all()
