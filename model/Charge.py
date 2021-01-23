from model.BaseModel import BaseModel
from datetime import datetime

from model.database import db


class ObjCharge(BaseModel):
    __tablename__ = "CHARGE"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pr_no = db.Column(db.String(100))
    charge_deptcode = db.Column(db.String(100))
    charge_pcode = db.Column(db.String(100))
    charge = db.Column(db.Numeric)
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.Integer)

    def __repr__(self):
        return '<CHARGE %r>' % self.id

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
