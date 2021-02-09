from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


from .config import Config



# instantiate our app
app = Flask(__name__)

# configuring the application
app.config.from_object(Config)

# configuring the db
db = SQLAlchemy()
db.init_app(app)



from .models import User

# try to drop db if present
try:
    db.drop_all()
    with app.app_context():
        db.create_all(app=app)
# create the db
except Exception as e:
    with app.app_context():
        db.create_all(app=app)
        
from .auth import auth  # it should be here and also the models after initialization of app as the circular error might come due to db import
# configure login manager
login_manager = LoginManager()
# which view will handle the login
login_manager.login_view = 'auth.login'
# initializing the login manager
login_manager.init_app(app)

# create a user loader method which will load user from the session


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)  # get by id


# registring the blueprint
app.register_blueprint(auth)
