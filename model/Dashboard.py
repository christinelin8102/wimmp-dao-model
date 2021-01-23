from model.BaseModel import BaseModel
from datetime import datetime

from model.database import db


class ObjDashboard(BaseModel):
    __tablename__ = "DASHBOARD"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.Integer)

    def __repr__(self):
        return '<DASHBOARD %r>' % self.id
