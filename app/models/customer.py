from flask import current_app
from sqlalchemy.orm import backref
from app import db
from datetime import datetime

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    registered_at = db.Column(db.DateTime, nullable=True)
    postal_code = db.Column(db.Integer)
    phone = db.Column(db.String)
    videos_checked_out_count = db.Column(db.Integer, default=0)
    videos = db.relationship("Rental", backref="customer", lazy=True)
    
    def to_json(self): 
        to_json = {
                "id": self.customer_id,
                "name": self.name,
                "registered_at": self.registered_at,
                "postal_code": self.postal_code, 
                "phone": self.phone,
                "videos_checked_out_count": self.videos_checked_out_count              
        }
        return to_json
    
    @classmethod
    def make_a_customer(cls, json, id): 
        return cls(customer_id=id,
                    name=json["name"],
                    postal_code=json["postal_code"],
                    registered_at=datetime.utcnow(), 
                    phone=json["phone"])