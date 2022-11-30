from market import app  # Importa var "app" do arquivo "__init__.py"
from flask_sqlalchemy import SQLAlchemy  # Importa SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin,LoginManager
"""                 ATENÇÃO!! - AVISOS IMPORTANTES!!
	A var "db", diferente do que é feito no vídeo, deve ser criada dentro do arquivo "models.py" e não no "__init__.py"!
	O código feito aqui está correto, o código do vídeo está desatualizado nesse quesito!
	O SQLITE NÃO ACEITA DADOS REPETIDOS. SE VOCÊ TENTAR ENVIAR UMA INFORMAÇÃO QUE JÁ ESTÁ REGISTRADA NO BANCO DE DADOS, O SITE RETORNARÁ ERRO.
"""
db = SQLAlchemy(app)  # Cria DB
# GETTERS AND SETTERS -  É um jeito de configurar a forma com que a gente recebe e envia um atributo(Questão de segurança)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login_page'
login_manager.login_message_category='info'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True)  # Cria coluna
	username = db.Column(db.String(length=30), nullable=False, unique=False)# Cria coluna - nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
	email_address = db.Column(db.String(length=12),nullable=False, unique=True)# Cria coluna - nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
	password_hash = db.Column(db.String(length=1024),nullable=False, unique=True)# Cria coluna - nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
	budget = db.Column(db.Integer(), nullable=False, default=1000)# Cria coluna - default=(Define valor padrão para o primeiro registro)
	items = db.relationship('Item', backref='owned_user',lazy=True)  # lazy=True(Obrigatório)

	@property
	def prettier_budget(self):
		if len(str(self.budget)) >=4:
			return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
		else:
			return f'{self.budget}$'
			
	@property
	def password(self):
		return self.password

	@password.setter
	def password(self, plain_text_password):
		self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
		print(self.password_hash)
		print("======================================================================\n\n\n\n\n\n\n\n")

	def check_password_correction(self, attempted_password):
		print(self.password_hash, attempted_password)
		return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Item(db.Model):  # Cria classe
	id = db.Column(db.Integer(), primary_key=True)  # Cria coluna
	# Cria coluna - nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
	name = db.Column(db.String(length=30), nullable=False, unique=True)
	price = db.Column(db.Integer(), nullable=False)  # Cria coluna
	# Cria coluna - nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
	barcode = db.Column(db.String(length=12), nullable=False, unique=True)
	# Cria coluna - nullable=(Habilita ou não textos vazios) | unique=(Habilita ou não somente textos unicos. Ex: Iphone10[Unico] e Iphone 10[Separado])
	description = db.Column(db.String(length=1024),nullable=False, unique=True)
	owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

	def __repr__(self):  # (????????????????????????????????????????????????)
		return f'Item {self.name}'


from market import routes  # Import the routes inside routes.py
