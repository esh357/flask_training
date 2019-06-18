from flask_wtf import FlaskForm
from wtforms import TextField, DecimalField, SelectField
from decimal import Decimal
from wtforms.validators import InputRequired, NumberRange


class ProductForm(FlaskForm):
    name = TextField('Name', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired(),
                                              NumberRange(min=Decimal('0.0'))])
    category = SelectField('Category', coerce=int, validators=[InputRequired()])
