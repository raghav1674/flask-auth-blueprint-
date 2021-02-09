from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user,logout_user

from . import auth
from ..models import User
from ..forms import RegsiterForm, LoginForm
from .. import db 

@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegsiterForm()
    if request.method == 'POST':
        # request method is post
        if form.validate_on_submit():
            # create a new user
            new_user = User(
                name=form.name.data,
                email=form.email.data
            )
            
            
            new_user.set_password(form.password.data)
            ## save to the db 
            db.session.add(new_user)
            ## commit 
            db.session.commit()
            
            # login successfull
            return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
        
            user = User.query.filter_by(email=email).first()
            if user and user.get_password(password):
                # if user exists then check for password, then redirect to welcome page
                login_user(user, remember=True)
                
                return render_template('dashboard.html',user=current_user)

        # credentails do not match
        return render_template('login.html', form=form)

    # if request is not post then also render same
    return render_template('login.html', form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))