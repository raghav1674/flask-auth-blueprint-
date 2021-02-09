from flask import Blueprint

# instantiating a blueprint 
auth = Blueprint('auth',__name__,template_folder='templates')

# importing the routes 
from . import routes 

