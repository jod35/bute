from . import app,db,bcrypt
from flask import render_template,request,redirect,url_for
from .models import User

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup',methods=['GET', 'POST'])
def create_account():
    return render_template('sign.html')

@app.route('/login',methods=['GET', 'POST'])
def sign_in():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')