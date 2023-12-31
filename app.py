#!/usr/bin/env python3
'''
Main app Module
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'

# Disable Flask-SQLAlchemy modification tracking
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)


if __name__=='__main__':
    app.run(debug=True)