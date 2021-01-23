from model.BaseModel import BaseModel
from datetime import datetime

from model.database import db


class ObjPurchaseOrderCharge(BaseModel):
    __tablename__ = "PURCHASE_ORDER_CHARGE"
    po_no = db.Column(db.String(100), primary_key=True)
    po_line_no = db.Column(db.String(10), primary_key=True)
    mmp_charge_code = db.Column(db.String(100), primary_key=True)
    mmp_charge = db.Column(db.Numeric)
    mmp_charge_in_ntd = db.Column(db.Numeric)
    mmp_charge_amount = db.Column(db.Numeric)
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.Integer)

    def __repr__(self):
        return '<PURCHASE_REQUESTS_DETAIL %r>' % self.id

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
