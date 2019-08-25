from flask import flash, request, url_for, redirect, session
from flask_login import login_user, logout_user, current_user

from webapp import login_manager, app
from webapp.auth.forms import LoginForm
from webapp.auth.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User.query.filter(User.name==form.name.data).first()
        if not user or user.password != form.password.data:
            flash("Invalid username or password", category='danger')
            return redirect('/')
        print("Logging in user", user)
        login_user(user)
        flash('Logged in successfully.', category='success')
    return redirect('/')


@app.route("/logout", methods=['POST'])
def logout():
    logout_user()
    return redirect('/')


@app.context_processor
def inject_login_form():
    if not current_user.is_authenticated:
        return dict(login_form=LoginForm(csrf_enabled=False))
    return {}
