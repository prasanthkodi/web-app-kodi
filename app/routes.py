from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models import User

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('layout.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    # Add login logic here
    return render_template('login.html')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    # Add signup logic here
    return render_template('signup.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))