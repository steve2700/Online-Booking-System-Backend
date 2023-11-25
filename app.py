#!/usr/bin/env python3
'''
Main app Module
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =''
SQLAlchemy(app)

