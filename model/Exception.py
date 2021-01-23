from model.BaseModel import BaseModel
from datetime import datetime

from model.database import db


class ObjException(BaseModel):
    __tablename__ = "EXCEPTION"
    exception_id = db.Column(db.Integer, primary_key=True)
    exception_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    send_alert = db.Column(db.Boolean)
    send_mail = db.Column(db.Boolean)
    mail_list = db.Column(db.Text)
    status = = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.Integer)

    def __repr__(self):
        return '<EXCEPTION %r>' % self.id

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
