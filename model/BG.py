from model.BaseModel import BaseModel
from datetime import datetime

from model.database import db


class ObjBG(BaseModel):
    __tablename__ = "BGS"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100))
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
