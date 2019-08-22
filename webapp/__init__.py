import os

from flask import Flask
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
print('GEtting from redis', redis_client.get('test'))

# import product blueprint
from webapp.product.views import product as product_blueprint
# Register a blue print
app.register_blueprint(product_blueprint)
# Create all required tables
db.create_all()
