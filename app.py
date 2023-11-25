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

# Import your models here
from backend.models.base_model import BaseModel
from backend.models.user import User
from backend.models.event import Even
from backend.models.admin import Admin
from backend.models.booking import Booking
from backend.models.event_attendees import event_attendees
from backend.models.venue import Venue