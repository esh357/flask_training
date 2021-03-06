from functools import wraps

from sqlalchemy.orm.util import join
from flask import (request, jsonify, Blueprint, render_template, flash,
                   redirect, url_for)

from webapp import db
from webapp.product.models import Product, Category
from webapp.product.forms import ProductForm, CategoryForm


product = Blueprint('product', __name__)


@product.app_template_filter('full_name')
def full_name_filter(product):
    return '{0} / {1}'.format(product['category'], product['name'])


@product.app_template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:])
    return '{0} {1}'.format(currency_code, amount)


def template_or_json(template=None):
    """Return a dict from your view and this will either pass it to a template
    or render json. Use like:
    @template_or_json('template.html')
    """
    def decorated(f):
        @wraps(f)
        def decorated_fn(*args, **kwargs):
            ctx = f(*args, **kwargs)
            if request.is_xhr or not template:
                return jsonify(ctx)
            else:
                return render_template(template, **ctx)
        return decorated_fn
    return decorated


@product.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@product.route('/')
@product.route('/home')
@template_or_json('home.html')
def home():
    '''
    if request.is_xhr:
        products = Product.query.all()
        return jsonify({
            'count': len(products)
        })
    return render_template('home.html')
    '''
    products = Product.query.all()
    return {'count': len(products)}


@product.route('/product/<string(minlength=2, maxlength=3):key>')
@product.route('/product/<id>')
def get_product(id):
    product = Product.query.get_or_404(id)
    return render_template('product.html', product=product)


@product.route('/products')
@product.route('/products/<int:page>')
def products(page=1):
    products = Product.query.paginate(page, 10, False).items
    return render_template('products.html', products=products)


@product.route('/product-create', methods=['GET', 'POST'])
def create_product():
    form = ProductForm(csrf_enabled=False)

    categories = [(c.id, c.name) for c in Category.query.all()]
    form.category.choices = categories

    if request.method == 'POST' and form.validate():
        name = form.name.data
        price = form.price.data
        category_name = form.category.data
        category = Category.query.get_or_404(form.category.data)
        if not category:
            category = Category(category_name)
        product = Product(name, price, category)
        db.session.add(product)
        db.session.commit()
        flash('The product {0} has been created'.format(name), 'success')
        return redirect(url_for('product.get_product', id=product.id))
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('product-create.html', form=form)


@product.route('/category-create', methods=['POST', 'GET'])
def create_category():
    form = CategoryForm(csrf_enabled=False)

    if form.validate_on_submit():
        name = form.name.data
        categories = Category.query.filter(Category.name == name).first()
        if categories:
            flash("Category {0} already exists.".format(name), "danger")
            return redirect(url_for("product.create_category"))
        category = Category(name)
        db.session.add(category)
        db.session.commit()
        flash("Category {0} is added successfully".format(name), "success")
        redirect(url_for("product.category", id=category.id))
    return render_template('category-create.html', form=form)


@product.route('/category/<id>')
def category(id):
    category = Category.query.get_or_404(id)
    return render_template('category.html', category=category)


@product.route('/categories')
def categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)


@product.route('/product-search')
@product.route('/product-serch/<int:page>')
def product_search(page=1):
    name = request.args.get('name')
    price = request.args.get('price')
    # company = request.args.get('company')
    category = request.args.get('category')
    products = Product.query
    if name:
        # SELECT * FROM product WHERE name like "%iPhone%"
        products = products.filter(Product.name.like('%' + name + '%'))
    if price:
        products = products.filter(Product.price == price)
    # if company:
    #     products = products.filter(Product.company.like('%' + company + '%'))
    if category:
        # SELECT * FROM product INNER JOIN category ON category.id = product.category_id 
        # WHERE category.name like "%Phone%"
        products = products.join(Category).filter(
            Category.name.like('%' + category + '%'))
    return render_template('products.html', products=products.paginate(page, 10).items)
