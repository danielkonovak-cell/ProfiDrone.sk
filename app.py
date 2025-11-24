from project import create_app   # ✅ import from the 'project' package
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db

app = create_app()

views = Blueprint('views', __name__)

# --- Main site pages (HTML templates) ---
@views.route('/')
def home():
    return render_template('lobby.html')

@views.route('/contact')
def contact():
    return render_template('Contact.html')

@views.route('/farmers')
def farmers():
    return render_template('Farmers.html')

# --- Authentication ---
@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('views.home'))
        else:
            flash('Invalid email or password.', 'error')

    return render_template('LogIn.html')

@views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if not username or not email or not password:
            flash('All fields are required.', 'error')
            return redirect(url_for('views.register'))

        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
            return redirect(url_for('views.register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('views.login'))

    return render_template('register.html')

@views.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('views.home'))

# --- Admin or test route ---
@views.route('/users')
@login_required
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
