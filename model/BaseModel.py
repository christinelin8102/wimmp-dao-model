from model.database import db

SUCCESS = 0
FAILURE = -1

class BaseModel(db.Model):
    __abstract__ = True
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            raise e
        else:
            return SUCCESS

    def update(self):
        try:
            db.session.merge(self)
            db.session.commit()
        except Exception as e:
            # print(e)
            db.session.rollback()
            return FAILURE
        else:
            return SUCCESS

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            # print(e)
            db.session.rollback()
            return FAILURE
        else:
            return SUCCESS

    def deleteById(self, id):
        try:
            od = self.query.get(id)
            if od != None:
                db.session.delete(od)
                db.session.commit()
        except Exception as e:
            # print(e)
            db.session.rollback()
            return FAILURE
        else:
            return SUCCESS

    @staticmethod
    def save_all(model_list):
        try:
            db.session.add_all(model_list)
            db.session.commit()
        except Exception as e:
            # print(e)
            db.session.rollback()
            return FAILURE
        else:
            return SUCCESS

    @staticmethod
    def delete_all(model_list):
        try:
            for model in model_list:
                db.session.delete(model)
            db.session.commit()
        except Exception as e:
            # print(e)
            db.session.rollback()
            return FAILURE
        else:
            return SUCCESS