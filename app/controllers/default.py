from flask import render_template
from app import app


@app.route('/index/<user>')
@app.route('/index', defaults={'user': None})
def index(user):
    return render_template('index.html', user=user)
