from datetime import datetime

from model.BaseModel import BaseModel
from model.database import db


class ObjPurchaseOrderDetail(BaseModel):
    __tablename__ = "PURCHASE_ORDER_DETAIL"
    po_no = db.Column(db.String(100), primary_key=True)
    po_line_no = db.Column(db.String(10), primary_key=True)
    pr_line_no = db.Column(db.String(10))
    description = db.Column(db.Text)
    specification = db.Column(db.Text)
    po_qty = db.Column(db.Numeric)
    unit = db.Column(db.String(100))
    po_price = db.Column(db.Numeric)
    po_line_amount = db.Column(db.Numeric)
    im_pn = db.Column(db.String(100))
    only_check_amount = db.Column(db.Boolean)
    im_confidential = db.Column(db.String(100))
    price_before_tax = db.Column(db.Numeric)
    po_price_in_ntd = db.Column(db.Numeric)
    cost_saving = db.Column(db.Numeric)
    category = db.Column(db.String(100))
    po_line_amount_in_ntd = db.Column(db.Numeric)
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(255))
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(255))

    def __repr__(self):
        return '<PURCHASE_ORDERS_LINE %r>' % self.id

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
