#!/usr/bin/env python3
"""Attended Events model"""
from app import db


event_attendees = db.Table(
    'event_attendees',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)