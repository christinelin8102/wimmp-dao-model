from datetime import datetime

from model.BaseModel import BaseModel
from model.database import db


class ObjPurchaseOrder(BaseModel):
    __tablename__ = "PURCHASE_ORDER"
    po_no = db.Column(db.String(30), primary_key=True)
    pr_no = db.Column(db.String(50))
    buyer_name = db.Column(db.String(255))
    cancel_reject_remark = db.Column(db.Text)
    po_date = db.Column(db.DateTime, None)
    vendor_code = db.Column(db.String(100))
    vendor_name = db.Column(db.String(255))
    vendor2_code = db.Column(db.String(100))
    vendor2_name = db.Column(db.String(255))
    tax_rate = db.Column(db.Numeric)
    delivery_term = db.Column(db.String(100))
    delivery_date = db.Column(db.DateTime, default=datetime.now())
    payment_term = db.Column(db.String(100))
    po_currency = db.Column(db.String(10))
    po_amount = db.Column(db.Numeric)
    po_type1 = db.Column(db.String(100))
    po_type2 = db.Column(db.String(100))
    po_flag = db.Column(db.String(100))
    reimburse = db.Column(db.Boolean, default=False)
    company = db.Column(db.String(255))
    site = db.Column(db.String(20))
    approve_flag = db.Column(db.String(100))
    po_approve_date = db.Column(db.DateTime, default=datetime.now())
    warranty = db.Column(db.String(100))
    charge_plant_code = db.Column(db.String(100))
    mmp_vendor_code = db.Column(db.String(100))
    mmp_vendor_name = db.Column(db.String(255))
    mmp_bg = db.Column(db.String(20))
    mmp_site = db.Column(db.String(20))
    po_amount_in_ntd = db.Column(db.Numeric)
    po_exch_rate = db.Column(db.Numeric)
    pcode_deptcode = db.Column(db.String(100))
    mmp_payment_code = db.Column(db.String(100))
    po_kpi_status = db.Column(db.Boolean)
    po_kpi_hour = db.Column(db.Numeric)
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(255))
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(255))

    def __repr__(self):
        return '<PURCHASE_ORDERS %r>' % self.id

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
