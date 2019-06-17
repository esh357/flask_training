import ccy
import datetime
from werkzeug import abort
from flask import render_template
from flask import Blueprint
from flask import request

from webapp.product.models import PRODUCTS


product_blueprint = Blueprint('product', __name__)


@product_blueprint.app_template_filter('full_name')
def full_name_filter(product):
    return '{0} / {1}'.format(product['category'], product['name'])


@product_blueprint.app_template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:])
    return '{0} {1}'.format(currency_code, amount)


@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
    timestamp = datetime.datetime.now()
    return render_template('home.html', products=PRODUCTS, timestamp=timestamp)


@product_blueprint.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)
