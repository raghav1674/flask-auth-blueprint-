from . import db 
from flask_login import UserMixin  # UserMixin class has implemented the methods which is required while using flask-Login
from werkzeug.security import generate_password_hash, check_password_hash

# User Model
class User(db.Model,UserMixin):
    user_id = db.Column(db.Integer,primary_key=True)
    
    name = db.Column(db.String(40))
    email = db.Column(db.String(60),unique=True)
    password = db.Column(db.String(130))
    
    
    # # UserMixin calls the get_id and search from id property
    def get_id(self):
        return str(self.user_id)
    
    # to store the password in encoded formatted. 
    def set_password(self,password):
        self.password  = generate_password_hash(password,method='sha256')
        
    # check for the hash and password entered. 
    def get_password(self,password):
        return check_password_hash(self.password,password)
    
    def __str__(self):
        return self.name