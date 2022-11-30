from market import app
from market.models import Item
from flask import render_template
@app.route('/')
def hello_world():
    return "<h1 style=\"color:blue\">Hello World!!</h1>"

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'

@app.route('/market')
def market_page():
    itemsDict=Item.query.all()
    return render_template('market.html', items=itemsDict)