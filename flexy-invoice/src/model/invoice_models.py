'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from google.appengine.ext import db
from model.model_utils import check_for_uniqueness
from model.user_models import UserEntity

class InvoiceEntity(db.Model):
    user = db.ReferenceProperty(reference_class = UserEntity, required = True, collection_name = 'invoices')

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
        
class CurrencyEntity(db.Model):
    """ Currency entity """
    
    name = db.StringProperty(required = True)
    symbol = db.StringProperty(required = True)
    
    @classmethod
    def create(cls, name, symbol):
        check_for_uniqueness(CurrencyEntity, 'symbol', symbol)
        return cls(name = name, symbol = symbol)
    
class ExchangeRateEntity(db.Model):
    """ Exchange rate between two currencies """
    from_currency = db.ReferenceProperty(reference_class = CurrencyEntity, required = True, collection_name = "to_currencies")
    to_currency = db.ReferenceProperty(reference_class = CurrencyEntity, required = True, collection_name = "from_currencies")
    date = db.DateProperty(required = True)
    rate = db.FloatProperty(required = True)
    
    @classmethod
    def create(cls, from_currency, to_currency, date, rate):
        """ Create a new exchange rate instance """
        return cls(from_currency = from_currency, to_currency = to_currency, date = date, rate = rate)
    