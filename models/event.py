#!/usr/bin/env python3
"""Event Entity Module"""
from .base_model import BaseModel
from app import db
from models.user import User
from datetime import datetime


class Event(BaseModel):
    '''Event model class'''
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    venue = db.relationship('Venue', backref='events')
    attendees = db.relationship(
        'User', secondary='event_attendees', backref=db.backref(
            'attended_events', lazy='dynamic'))

    @classmethod
    def get_events_by_user_id(cls, user_id):
        """Retrieve events associated with a specific user"""
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def get_upcoming_events(cls):
        """Retrieve upcoming events"""
        return cls.query.filter(
            db.and_(cls.date >= datetime.today()
                    .date(), cls.time >= datetime.now().time())).all()

    @classmethod
    def get_event_details(cls, event_id):
        """Retrieve details of a specific event"""
        return cls.query.get(event_id)

    @classmethod
    def attend_event(cls, user_id, event_id):
        """Mark a user as attending a specific event"""
        event = cls.query.get(event_id)
        if event:
            user = User.query.get(user_id)
            if user:
                event.attendees.append(user)
                db.session.commit()
