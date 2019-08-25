import datetime
from webapp import db, admin
from flask_admin.contrib.sqla import ModelView


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('products',
                                                              lazy='dynamic'))

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product: {self.name}"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Category: {self.name}"

admin.add_view(ModelView(Product, db.session, category="Products"))
admin.add_view(ModelView(Category, db.session, category="Products"))
