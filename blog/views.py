from . import app,db,bcrypt
from flask import render_template,request,redirect,flash,url_for

from .models import User

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup',methods=['GET', 'POST'])
def create_account():
    if request.method=='POST':
        full_name=request.form.get('full_name')
        username=request.form.get('username')
        gender=request.form.get('gender')
        email=request.form.get('email')
        password=request.form.get('password')
        confirm=request.form.get('confirm')

        new_user=User(
            full_name=full_name,
            username=username,
            email=email,
            gender=gender,
            password=bcrypt.generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created Successfully')
        return redirect(url_for('create_account'))
        
    return render_template('sign.html')

@app.route('/login',methods=['GET', 'POST'])
def sign_in():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')