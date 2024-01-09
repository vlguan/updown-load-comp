from flask import Blueprint, render_template

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def home():
    return render_template('frontend/home.html')
