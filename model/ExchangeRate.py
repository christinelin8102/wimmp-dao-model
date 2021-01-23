from datetime import datetime

from model.BaseModel import BaseModel
from model.database import db


class ObjExchangeRate(BaseModel):
    __tablename__ = "EXCHANGE_RATE"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    kurst = db.Column(db.String(5))
    valid_from = db.Column(db.DateTime)
    ratio_from = db.Column(db.Numeric)
    currency_from = db.Column(db.String(5))
    ratio_to = db.Column(db.Numeric)
    currency_to = db.Column(db.String(5))
    rate = db.Column(db.Numeric)
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(255))
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(255))

    def __repr__(self):
        return '<EXCHANGE_RATE %r>' % self.id

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
