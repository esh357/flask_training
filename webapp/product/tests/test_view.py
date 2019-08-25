import unittest
from unittest.mock import patch, MagicMock

from webapp import app, db, session, Category, Product
from webapp.auth.models import User, Role
import json

ctx = app.app_context()
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
app.secret_key = 'testing'
app.config['SESSION_TYPE'] = 'filesystem'

ctx.push()

class ProductViewTest(unittest.TestCase):
	def setUp(self):
		db.create_all()
		category = Category(name='Test')
		product_1 = Product(name="Test Product 1", category=category,
							price=10)
		product_2 = Product(name="Test Product 2", category=category,
							price=10)
		db.session.add_all([category, product_1, product_2])
		db.session.flush()
		assert Category.query.count() == 1
		assert Product.query.count() == 2

	@patch("flask.request")
	def test_get_products(self, request):
		request.accept_languages = MagicMock()
		request.accept_languages.best = "en"
		with app.test_client() as client:
			response = client.get('/products')
			assert response.status.startswith('200')

	def tearDown(self):
		db.session.rollback()
		assert User.query.count() == 0
		db.drop_all()


if __name__ == '__main__':
	unittest.main()