from flask import Flask, render_template, redirect, url_for, session
from forms import RegistrationForm
from models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create and save the user
        return redirect(url_for('secret'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login form code goes here
    pass

@app.route('/secret')
def secret():
    return "You made it!"

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/users/<username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first()

    if user:
        # Render the user profile template with the retrieved information
        return render_template('user_profile.html', user=user)
    else:
        # User not found, handle the error or redirect to an appropriate page
        return redirect(url_for('index'))