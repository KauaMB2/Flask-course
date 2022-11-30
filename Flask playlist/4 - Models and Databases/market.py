from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),nullable=False,unique=True)#nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
    price=db.Column(db.Integer(),nullable=False)
    barcode=db.Column(db.String(length=12),nullable=False,unique=True)#nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
    description=db.Column(db.String(length=1024),nullable=False,unique=True)#nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
    
    def __repr__(self):
        return f'Item {self.name}'
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
#http://127.0.0.1:5000/

#Commands for sqlite:
#
#Acessing
# from market import app,db
# app.app_context().push()
# db.create_all()
#
#Show
# from market import Item
# Item.query.all()
#
#Add
# from market import Item
# varName=Item(name="Keyboard",price=150,barcode='231985128446',description='description')
# db.session.add(varName)
# db.session.commit()
#
#Search
# for item in Item.query.filter_by(price=500):
#     item.name