'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from google.appengine.ext import db
from model.model_utils import check_for_uniqueness
from model.user_models import UserEntity

class InvoiceEntity(db.Model):
    user = db.ReferenceProperty(reference_class = UserEntity, required = True, collection_name = 'invoices')
    
    @classmethod
    def create(cls, user):
        return cls(user = user)

class InvoiceItemEntity(db.Model):
    @classmethod
    def create(cls, invoice, description, price, quantity):
        """ 
            Create a new invoice item
            
            PARAMETERS:
            - invoice: the invoice the item is added to
            - description: the item description
            - price: the unit price
            - quantity: number of units
        """
        return cls(invoice = invoice, description = description, price = price, quantity = quantity)
