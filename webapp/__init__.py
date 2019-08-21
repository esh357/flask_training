from flask import Flask

from webapp.hello.views import hello
from webapp.product.views import product_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(hello)
    app.register_blueprint(product_blueprint)
    return app


app = create_app()


