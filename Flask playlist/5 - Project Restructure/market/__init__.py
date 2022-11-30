from flask import Flask#Import flask
app = Flask(__name__)#Cria aplicação
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'#Encontra o banco de dados(NECESSÁRIO)

from market import routes#Importa as rotas(NECESSÁRIO)