#!/usr/bin/env python3
"""Admin Entity model"""
from .base_model import BaseModel
from app import db
import bcrypt


class Admin(BaseModel):
    """Admin entity class"""

    __tablename__ = "admins"

    # Override the id attribute to have a different type
    id = db.Column(
        db.String(60), primary_key=True, unique=True, nullable=False
    )

    # Define columns for the Admin table
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    _password = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    # Relationship with Event model
    event = db.relationship(
        "Event", backref="admin", cascade="all, delete-orphan", lazy=True
    )

    @property
    def full_name(self):
        """Returns the admin full name"""
        return f"{self.first_name} {self.last_name}"

    @property
    def password(self):
        """Returns the hashed password"""
        return self._password

    @password.setter
    def password(self, password):
        """Sets the hashed password"""
        self._password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        """Verifies if the provided password matches the hashed password"""
        return bcrypt.checkpw(
            password.encode('utf-8'), self._password.encode('utf-8'))

    def format(self):
        """Format the Admin object's attributes as a dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'company': self.company,
            'position': self.position,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': self.full_name,
        }

    def __repr__(self):
        """Return a string representation of the Admin object"""
        return f"Id: {self.id}, Username: {
            self.username}, Name: {self.full_name}, Email: {self.email}"
