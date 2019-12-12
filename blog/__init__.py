from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from .config import DevConfig


app=Flask(__name__)
app.config.from_object(DevConfig)

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager()
login_manager.init_app(app)
migrate=Migrate(app,db)

from . import views