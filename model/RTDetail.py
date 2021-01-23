from model.BaseModel import BaseModel
from datetime import datetime

from model.database import db


class ObjRTDetail(BaseModel):
    __tablename__ = "RT_DETAIL"
    rt_no = db.Column(db.Integer, primary_key=True)
    rt_line_no = db.Column(db.Integer, primary_key=True)
    rt_qty = db.Column(db.Numeric)
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.Integer)

    def __repr__(self):
        return '<RT_LINES %r>' % self.id

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
