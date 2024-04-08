from app import app
from flask import render_template, flash, redirect, url_for
from flask import render_template
from app.forms import RegisterForm, AddProductForm



@app.route('/')
@app.route('/home')
def index():
    
    
    """Index URL"""
    return render_template('shop.html', title='Shop Page')
    
@app.route('/register', methods=['GET','POST'])
def register():
    
    
    """Register URL"""  
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You Have Been Successfuly Registered! ')
    return render_template('register.html', title='register', form=form)
    
@app.route('/add_product', methods=['GET','POST'])
def add_product():
    
    
    """Add Product URL"""
    form = AddProductForm()
    if form.validate_on_submit():
        flash(f'Product added ')
        return redirect(url_for('index'))
    return render_template('add_product.html', title='Add Product Page', form=form)


# 