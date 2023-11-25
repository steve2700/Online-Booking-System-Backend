#!/usr/bin/env python3
"""Booking Entity model"""
from .base_model import BaseModel
from app import db
from models.user import User
from models.event import Event
from datetime import datetime

class Booking(BaseModel):
    '''Booking model class'''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False, default=datetime.now)

    user = db.relationship('User', backref='bookings')
    event = db.relationship('Event', backref='bookings')

    def __repr__(self):
        """Return a string representation of the Booking object"""
        return f"Booking ID: {self.id}, User: {self.user.username}, Event: {self.event.event_name}, Booking Date: {self.booking_date}"
