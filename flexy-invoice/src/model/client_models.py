'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from google.appengine.ext import db
from model.invoice_models import CurrencyEntity
from model.user_models import UserEntity

class ClientEntity(db.Model):
    user = db.ReferenceProperty(reference_class = UserEntity, required = True, collection_name = 'clients')
    name = db.StringProperty(required = True)
    address = db.PostalAddressProperty(required = True)
    email = db.EmailProperty(required = True)
    default_currency = db.ReferenceProperty(reference_class = CurrencyEntity)
    
    @classmethod
    def create(cls, name, address, email, default_currency):
        return cls(name = name, address = address, email = email, default_currency = default_currency)
        
class ClientContactEntity(db.Model):
    name = db.StringProperty(required = True)
    email = db.EmailProperty()
    
    @classmethod
    def create(cls, client, name, email):
        return cls(client, name = name, email = email)
    