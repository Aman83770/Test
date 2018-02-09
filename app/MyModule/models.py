from app import db
from sqlalchemy import event
from app.models import *
from controller import after_entry_insert, after_entry_update

class MyTable(Base):
    __tablename__ = 'my_table'
    id =        db.Column(db.Integer,primary_key=True)

    name = db.Column(db.String(64))
    gender = db.Column(db.Enum('M','F'))
    age = db.Column(db.Integer)

    def import_data(self,data):
        try:

            if 'input_name' in data:
                self.name = data['input_name']

            self.gender = data['input_gender']

            self.age = data['input_age']

            return self

        except Exception as e:

            return str(e)


event.listen(MyTable, 'after_insert', after_entry_insert)
event.listen(MyTable, 'after_update', after_entry_update)

