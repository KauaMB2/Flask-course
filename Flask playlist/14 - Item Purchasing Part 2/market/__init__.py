from flask import Flask#Import flask
app = Flask(__name__)#Cria aplicação
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'#Encontra o banco de dados(NECESSÁRIO)
app.config['SECRET_KEY']='829de852066b68880f990c50'#Uma camada a mais de segurança em relação ao formulário



from market import routes#Importa as rotas(NECESSÁRIO)