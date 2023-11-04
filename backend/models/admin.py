#!/usr/bin/env python3
'''
Admin entity Module
'''
from app import db
from event import Event


class Admin(db.Model):
    '''Amin entity class'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    position = dc.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    events = db.ralationship('Event', backref='admin', lazy=True)
    
    @property
    def full_name(self):
        '''Returns the admin full name'''
        return f'{self.first_name} {self.last_name}'