from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("app.config.Config")

db = SQLAlchemy(app)

class people(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    lastname = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    address = db.Column(db.VARCHAR,nullable=True)
    reference_address = db.Column(db.VARCHAR,nullable=True)
    phone_number = db.Column(db.String(20),nullable=True)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def save(self):
        data = people(name=self.name,lastname=self.lastname,
                email = self.email, address = self.address,
                reference_address = self.reference_address,
                phone_number = self.phone_number)

        db.session.add(data)
        db.session.commit()

    def update(self,pk):
        data = people.query.filter_by(id=pk).first()
        data.name=self.name
        data.lastname=self.lastname
        data.email=self.email
        data.address=self.address
        data.reference_address=self.reference_address
        data.phone_number=self.phone_number
        db.session.commit()

    def delete(pk):
        person = people.query.filter_by(id=pk).first()
        db.session.delete(person)
        db.session.commit()
