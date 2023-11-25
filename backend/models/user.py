#!/usr/bin/env python3
"""User Entity Module"""
from .base_model import BaseModel
from backend import db


class User(BaseModel):
    """User model"""

    # Use the default behavior for the table name
    # __tablename__ = "users"

    # Use an integer type for the primary key
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)

    # Adjust the length of string columns based on your requirements
    username = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    access_token = db.Column(db.String(100), nullable=False)
    refresh_token = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(255), nullable=False)
    
    attended_events = db.relationship(
        'Event', secondary='event_attendees', backref=db.backref(
            'attendees', lazy='dynamic')
    )

    def __repr__(self):
        """Return a string representation of the User object"""
        return (
            f"Id: {self.id}, Username: {self.username}, "
            f"Name: {self.name}, Email: {self.email}"
            )

    # Override the format method to return user attributes as a dictionary
    def format(self):
        """Return a dictionary representation of the User object"""
        return {
            "username": self.username,
            "name": self.name,
            "email": self.email,
            "avatar": self.avatar,
        }