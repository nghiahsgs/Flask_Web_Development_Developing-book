from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

username = 'root'
password = ''
hostname = 'localhost'
database = 'test_mysqlalchemy'

# username = 'nghiahsgs4'
# password = '261997'
# hostname = '45.77.36.114'
# database = 'test_mysqlalchemy'


DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s'%(username, password, hostname, database)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref='role') 
    #1 user.role la ra role
    #1 role.users => cac user co role nhu vay => one to many
    def __repr__(self):
        return "<Role %r>"%self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index= True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return "<User %r>"%self.username


# @app.route('/')
# def index():
#     return "hello index" 

# app.run(debug=True, port=3002)