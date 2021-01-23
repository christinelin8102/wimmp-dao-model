from datetime import datetime

from model.BaseModel import BaseModel
from model.database import db


class ObjPaymentTerm(BaseModel):
    __tablename__ = "PAYMENT_TERM"

    payment_term = db.Column(db.String(100), primary_key=True)
    payment_code = db.Column(db.String(100))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(255))
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(255))

    def __repr__(self):
        return '<PAYMENT_TERM %r>' % self.id

    def create(self, data):
        db.session.add(data)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, id):
        od = self.query.get(id)
        if None != od:
            db.session.delete(od)
            return db.session.commit()
