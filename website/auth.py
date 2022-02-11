from flask import Blueprint, render_template, request, flash, redirect, url_for ,session
from .models import User,Profiles
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')


        user = User.query.filter_by(email=email).first()

        user_username = User.query.filter_by(username=email).first()
        if not user:
            user=user_username
        session['uname']=user.username
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        full_name = request.form.get('firstName')
        uname = request.form.get('uname')
        college_name = request.form.get('college_name')
        gender = request.form.get('gender')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        user_name = User.query.filter_by(username=uname).first()
        if user_name:
            flash('Username Already Exists', category='error')
        elif len(uname)<6:
            flash('Username should atleast consists of 6 characters',category='error')
        elif user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(full_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, username=uname,full_name=full_name, password=generate_password_hash(
                password1, method='sha256'),gender=gender,institution_name=college_name)
            session['uname'] = uname
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            pf = Profiles(codechef="", codeforces="", atcoder="", hackerrank="", leetcode="",
                          hackerearth="", github="", devfolio="", pwebsite="",
                          linkedin="",
                          city="", country="", user_id=current_user.id)
            db.session.add(pf)
            db.session.commit()

            return redirect(url_for('views.home'))
    
    # print('Gopal')
    try:
        name=current_user.full_name
        return render_template("profile.html",user=current_user)
    except:
        return render_template("sign_up.html",user=current_user)