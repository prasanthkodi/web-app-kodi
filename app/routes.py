from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import TitanicData

# Create a Blueprint for the main routes
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('layout.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # Redirect to dashboard if the user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the user exists
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)  # Log the user in
            flash('Login successful!', 'success')
            return redirect(url_for('main.dashboard'))  # Redirect to dashboard
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    # Redirect to dashboard if the user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the username or email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('Username or email already exists.', 'danger')
            return redirect(url_for('main.signup'))

        # Hash the password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Create a new user
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('main.login'))

    return render_template('signup.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    passengers = TitanicData.query.all()  # Fetch first 10 records
    return render_template('dashboard.html', passengers=passengers)


@bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.index'))
    