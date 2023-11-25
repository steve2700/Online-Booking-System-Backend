#!/usr/bin/env python3
'''
Initializer Module
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'

# Disable Flask-SQLAlchemy modification tracking
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

# Import your models here
from models.base_model import BaseModel
from models.user import User
from models.event import Event
from models.admin import Admin
from models.booking import Booking
from models.event_attendees import event_attendees
from models.venue import Venue