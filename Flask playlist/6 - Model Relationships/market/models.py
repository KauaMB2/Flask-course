from market import app#Importa var "app" do arquivo "__init__.py"
from flask_sqlalchemy import SQLAlchemy#Importa SQLAlchemy 

"""                 ATENÇÃO!! - IMPORTANTE!!
    A var "db", diferente do que é feito no vídeo, deve ser criada dentro do arquivo "models.py" e não no "__init__.py"!
    O código feito aqui está correto, o código do vídeo está desatualizado nesse quesito!
"""
db=SQLAlchemy(app)#Cria DB

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)#Cria coluna
    username=db.Column(db.String(length=30),nullable=False,unique=True)#Cria coluna - nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
    email_address=db.Column(db.String(length=12),nullable=False,unique=True)#Cria coluna - nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
    password_hash=db.Column(db.String(length=1024),nullable=False,unique=True)#Cria coluna - nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
    budget=db.Column(db.Integer(),nullable=False,default=1000)#Cria coluna - default=(Define valor padrão para o primeiro registro)
    items=db.relationship('Item',backref='owned_user',lazy=True)#lazy=True(Obrigatório)

class Item(db.Model):#Cria classe
    id=db.Column(db.Integer(),primary_key=True)#Cria coluna
    name=db.Column(db.String(length=30),nullable=False,unique=True)#Cria coluna - nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
    price=db.Column(db.Integer(),nullable=False)#Cria coluna
    barcode=db.Column(db.String(length=12),nullable=False,unique=True)#Cria coluna - nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
    description=db.Column(db.String(length=1024),nullable=False,unique=True)#Cria coluna - nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
    owner=db.Column(db.Integer(),db.ForeignKey('user.id'))

    def __repr__(self):#(????????????????????????????????????????????????)
        return f'Item {self.name}'
    
from market import routes#Import the routes inside routes.py