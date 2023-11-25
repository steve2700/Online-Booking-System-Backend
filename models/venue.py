#!/usr/bin/env python3
"""Venue Entity Module"""
from .base_model import BaseModel
from app import db
from models.event import Event

class Venue(BaseModel):
    '''Venue entity class'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    events = db.relationship('Event', backref='venue', lazy=True)

    @classmethod
    def get_events_by_venue_id(cls, venue_id):
        """Retrieve events associated with a specific venue"""
        venue = cls.query.get(venue_id)
        if venue:
            return venue.events
        return []

    # Override the format method to return venue attributes as a dictionary
    def format(self):
        """Return a dictionary representation of the Venue object"""
        return {
            "id": self.id,
            "name": self.name,
        }
