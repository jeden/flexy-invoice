'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from google.appengine.ext import db
from model.user_models import UserEntity
from model.client_models import ClientEntity
from model.domain_models import CurrencyEntity
from flexy.model.db_model import DbModel

class InvoiceEntity(DbModel):
    ''' Invoice '''
    user = db.ReferenceProperty(reference_class = UserEntity, required = True, collection_name = 'invoices')
    client = db.ReferenceProperty(reference_class = ClientEntity, required = True, collection_name = 'invoices')
    currency = db.ReferenceProperty(reference_class = CurrencyEntity, required = True)
    invoice_no = db.StringProperty(required = True)
    invoice_date = db.DateProperty(required = True)
    sale_date = db.DateProperty(required = True)
    
    # Calculated fields
    subtotal = db.FloatProperty(default = 0.0)
    total = db.FloatProperty(default = 0.0)
    
    @classmethod
    def create(cls, user, client, currency, invoice_no, invoice_date, sale_date):
        return cls(user = user, client = client, currency = currency, invoice_no = invoice_no, invoice_date = invoice_date, sale_date = sale_date)

class InvoiceItemEntity(DbModel):
    ''' Invoice item '''
    invoice = db.ReferenceProperty(reference_class = InvoiceEntity, collection_name = 'invoice_items') 
    description = db.StringProperty(required = True)
    unit_price = db.FloatProperty(required = True)
    quantity = db.FloatProperty(required = True)
    
    @classmethod
    def create(cls, description, unit_price, quantity):
        """ 
            Create a new invoice item
            
            PARAMETERS:
            - invoice: the invoice the item is added to
            - description: the item description
            - unit_price: the unit price
            - quantity: number of units
        """
        return cls(description = description, unit_price = unit_price, quantity = quantity)

    def attach_to_invoice(self, invoice):
        ''' 
            Attach the item to the invoice
            When a model is created, the referenced properties must already be saved.
            Since the invoice is saved at a later stage after items creation, this method allows
            proper attachment to invoice right before saving invoice and items
        '''
        self.parent = invoice
        self.invoice = invoice