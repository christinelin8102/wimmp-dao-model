from model.BaseModel import BaseModel
from datetime import datetime

from model.database import db


class ObjApproverList(BaseModel):
    __tablename__ = "APPROVER_LIST"
    pr_no = db.Column(db.String(100))
    approver_level = db.Column(db.String(5))
    approver_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.Integer)

    def __repr__(self):
        return '<APPROVER_LIST %r>' % self.id

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
