from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://rootAdi@0901@3306/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#app.config ['SECRET_KEY']='28010591275abf9535aaec13'
db = SQLAlchemy(app)
from myproject import route 
