#!/usr/bin/env python3
'''
Venue entity Module
'''
from app import db
from event import Event


class Venue(db.Model):
    '''Venue entity class'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    events = db.relationship('Event', backref='venue', lazy=True)
