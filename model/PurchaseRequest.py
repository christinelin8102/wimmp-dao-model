from model.BaseModel import BaseModel
from datetime import datetime

from model.database import db


class ObjPurchaseRequest(BaseModel):
    __tablename__ = "PURCHASE_REQUEST"
    pr_no = db.Column(db.String(100), primary_key=True)
    pr_currency = db.Column(db.String(10))
    pr_approve_date = db.Column(db.DateTime, default=datetime.now())
    applicant = db.Column(db.String(100))
    applicant_dept = db.Column(db.String(100))
    pr_type = db.Column(db.String(100))
    sub_type = db.Column(db.String(100))
    pr_buyer_datetime = db.Column(db.DateTime, None)
    pr_before_buyer_datetime = db.Column(db.DateTime, default=datetime.now())
    pr_exch_rate = db.Column(db.Numeric)
    pr_remark = db.Column(db.Text)
    pr_kpi_status = db.Column(db.Boolean)
    pr_kpi_hour = db.Column(db.Numeric)
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.Integer)

    def __repr__(self):
        return '<PURCHASE_REQUESTS %r>' % self.id

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
