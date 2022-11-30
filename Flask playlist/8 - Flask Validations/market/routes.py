from market import app
from market.models import Item,User,db
from flask import render_template,redirect,url_for
from market.forms import RegisterForm

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

@app.route('/register',methods=['GET','POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            print(f'There was an error with creating a user: {err_msg}')
    return render_template('register.html',form=form)

