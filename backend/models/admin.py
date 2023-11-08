#!/usr/bin/env python3
"""Admin entity Module"""

from backend import db
import bcrypt


class Admin(db.Model):
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
        self._password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        """Verifies if the provided password matches the hashed password"""
        return bcrypt.checkpw(password.encode('utf-8'), self._password.encode('utf-8'))

    def __repr__(self):
        """Return a string representation of the Admin object"""
        return "Id: {}, Username: {}, Name: {}, Email: {}".format(
            self.id, self.username, self.full_name, self.email
        )

