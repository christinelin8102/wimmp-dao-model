from model.BaseModel import BaseModel
from datetime import datetime

from model.database import db


class ObjPaymentApplication(BaseModel):
    __tablename__ = "PAYMENT_APPLICATION"
    po_no = db.Column(db.String(100), primary_key=True)
    fin_pm_no = db.Column(db.String(100), primary_key=True)
    fin_payment_date = db.Column(db.DateTime, None)
    order_type = db.Column(db.String(100))
    hsf = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.Integer)

    def __repr__(self):
        return '<PAYMENT_APPLICATION %r>' % self.id

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
