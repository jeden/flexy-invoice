'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from google.appengine.ext import db
from model.user_models import UserEntity
from model.domain_models import CurrencyEntity, LanguageEntity
from flexy.model.db_model import DbModel

class ClientEntity(DbModel):
    """
        An entity that can be invoiced.
    """
    user = db.ReferenceProperty(reference_class = UserEntity, required = True, collection_name = 'clients')
    name = db.StringProperty(required = True)
    address = db.PostalAddressProperty(required = True)
    email = db.EmailProperty(required = True)
    default_currency = db.ReferenceProperty(reference_class = CurrencyEntity)
    default_language = db.ReferenceProperty(reference_class = LanguageEntity)
    
    @classmethod
    def create(cls, user, name, address, email, default_currency, default_language):
        return cls(user = user, name = name, address = address, email = email, default_currency = default_currency, default_language = default_language)
    
    def __repr__(self):
        return self.name
        
class ClientContactEntity(DbModel):
    """
        A client contact  - usually the person the invoice is sent to.
    """
    client = db.ReferenceProperty(reference_class = ClientEntity, required = True, collection_name = "contacts")
    name = db.StringProperty(required = True)
    email = db.EmailProperty()
    
    @classmethod
    def create(cls, client, name, email):
        return cls(client = client, name = name, email = email)
    