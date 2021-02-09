import os 

# configuration of our application

class Config(object):
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x89+c$\xeddth\xf4\xc7O\xda\x9e\xab\xc3\xd6'
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    
    
    
# get random string
# python -c "import os; print(os.urandom(16))"