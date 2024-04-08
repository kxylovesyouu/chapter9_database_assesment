from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Email


class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username', validators= [DataRequired(), Length(1, 64)])
    email = StringField('Email', validators= [DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
class AddProductForm(FlaskForm):
    """ Add Product Form """
    product_name = StringField('Product Name', validators= [DataRequired(), Length(1, 64)])
    product_description = StringField('Product Description', validators= [DataRequired(), Length(1, 64)])
    stock_available = SelectField('Stock Available', choices = [(1,1),(2,2),(3,3),(4,4),(5,5)])
    submit = SubmitField('Add Product')