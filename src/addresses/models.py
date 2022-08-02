from datetime import datetime, timezone
from src import db


class Address(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255))
    phone_number = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    street_address = db.Column(db.String(255))
    created_at = db.Column(
        db.DateTime, default=datetime.now(timezone.utc), nullable=False
    )

    def __init__(self, first_name, last_name, phone_number, email, street_address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.street_address = street_address

    def __repr__(self):
        return f"Address({self.first_name}, {self.last_name}, {self.phone_number}, {self.email}, {self.street_address})"
