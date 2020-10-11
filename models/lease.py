import datetime
from db import db
from models.property import PropertyModel
from models.user import UserModel
from models.tenant import TenantModel
from models.base_model import BaseModel


class LeaseModel(BaseModel):
    __tablename__ = "lease"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    propertyID = db.Column(db.Integer, db.ForeignKey('properties.id'))
    tenantID = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)
    occupants = db.Column(db.Integer)
    dateTimeStart = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    dateTimeEnd = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def json(self):
        property = PropertyModel.find_by_id(self.propertyID)

        return {
          'id': self.id,
          'name':self.name,
          'propertyID': property.json(),
          'tenantID': self.tenant.json(),
          'dateTimeStart': self.dateTimeStart.strftime("%m/%d/%Y %H:%M:%S"),
          'dateTimeEnd': self.dateTimeEnd.strftime("%m/%d/%Y %H:%M:%S"),
          'occupants': self.occupants
        }
