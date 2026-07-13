from flask import Blueprint, request, redirect, url_for, session, flash, render_template
from core.database import USERS

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('cv.dashboard'))
    return render_template('login.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email in USERS and USERS[email] == password:
        session['user'] = email
        return redirect(url_for('cv.dashboard'))
    
    flash('Email atau password salah!', 'danger')
    return redirect(url_for('auth.index'))

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.index'))