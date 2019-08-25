import unittest

from webapp import app, db, session
from webapp.auth.models import User, Role
import json

ctx = app.app_context()
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
app.secret_key = 'testing'
app.config['SESSION_TYPE'] = 'filesystem'

ctx.push()

class UserViewTest(unittest.TestCase):
	def setUp(self):
		db.create_all()
		role = Role(name='Test')
		user1 = User(id=1, name='one', password='test', role=role)
		user2 = User(id=2, name='two', password='test', role=role)
		db.session.add_all([role, user1, user2])
		db.session.flush()
		assert User.query.count() > 0

	def test_login_and_logout(self):
		with app.test_client() as client:
			response = client.post('/login', data=dict(name='one',
												   password='test'))
			assert session['user_id'] == 1
			assert response.status.startswith('302')
			response = client.post('/logout', data=dict())
			assert 'user_id' not in session
			assert response.status.startswith('302')


	def test_fail_login(self):
		with app.test_client() as client:
			client.post('/login', data=dict(name='one', password='test2'))
			assert 'user_id' not in session

	def tearDown(self):
		db.session.rollback()
		assert User.query.count() == 0
		db.drop_all()


if __name__ == '__main__':
	unittest.main()