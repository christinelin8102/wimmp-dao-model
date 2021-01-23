from model.BaseModel import BaseModel
from datetime import datetime

from model.database import db


class ObjExceptionAlert(BaseModel):
    __tablename__ = "EXCEPTION_ALERT"
    alert_id = db.Column(db.Integer, primary_key=True)
    triggered_date = db.Column(db.DateTime)
    assigned_to = db.Column(db.String(100))
    processed_by = db.Column(db.String(100))
    plant_code = db.Column(db.String(100))
    po_no = db.Column(db.String(100))
    po_line_no = db.Column(db.String(10))
    po_currency = db.Column(db.String(10))
    po_price = db.Column(db.Numeric)
    po_line_amount = db.Column(db.Numeric)
    exception_id = db.Column(db.Integer)
    rule_result = db.Column(db.String(255))
    is_reasonable = db.Column(db.Boolean)
    notes = db.Column(db.Text)
    files_link = db.Column(db.String(255))
    status = db.Column(db.String(255))
    vendor_code = db.Column(db.String(100))
    vendor_name = db.Column(db.String(255))
    pr_remark = db.Column(db.Text)
    mmp_bg = db.Column(db.String(20))
    mmp_site = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.Integer)

    def __repr__(self):
        return '<EXCEPTION_ALERT %r>' % self.id

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
