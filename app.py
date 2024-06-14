from flask import Flask, render_template, redirect, url_for, session
from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime
import os


load_dotenv('.env')
app = Flask(__name__)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    last_active = db.Column(db.DateTime(datetime.utcnow()))

    def check_user(username, password):
        pass
    
class Glossary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String, nullable=False)
    definition = db.Column(db.String, nullable=False)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('administrator.html')

@app.route('/logout')
def logout():
    session.pop('username', default=None)
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(port=5001)