'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from model.invoice_models import InvoiceEntity, InvoiceItemEntity
from logic.client_manager import ClientManager
from logic.currency_manager import CurrencyManager
from google.appengine.ext import db

class InvoiceManager:
    """ Invoice creation and management """
    
    def __init__(self, user):
        self._user = user
        self._invoice = None
        self._invoice_items = []
    
    def create(self, client_id, currency_id, invoice_no, invoice_date, sale_date):
        '''
            Create a new invoice
        '''
        self._invoice_items = []
        
        client = ClientManager.find_by_id(client_id)
        currency = CurrencyManager.find_by_id(currency_id)
        
        self._invoice = InvoiceEntity.create(
                                       user = self._user,
                                       client = client,
                                       currency = currency,
                                       invoice_no = invoice_no,
                                       invoice_date = invoice_date,
                                       sale_date = sale_date
                                    )

        return self._invoice
    
    def add_invoice_item(self, description, quantity, unit_price):
        ''' Add an item to the current invoice '''
        invoice_item = InvoiceItemEntity.create(description = description, quantity = quantity, unit_price = unit_price)
        self._invoice_items.append(invoice_item)

        invoice_item.subtotal = invoice_item.unit_price * invoice_item.quantity
        invoice_item.total = invoice_item.subtotal
        
        self._invoice.subtotal += invoice_item.subtotal
        self._invoice.total += invoice_item.total
        
        return invoice_item

    def save(self):
        ''' Save the invoice along with its invoice items '''
        
        # Save the invoice
        self._invoice.put()
        
        # Save the invoice items
        for invoice_item in self._invoice_items:
            invoice_item.attach_to_invoice(self._invoice)
        db.put(self._invoice_items)    
        
    @property
    def invoice(self):
        ''' Return the current invoice '''
        return self._invoice
    
    @property
    def invoice_items(self):
        ''' Return the invoice items '''
        return self._invoice_items
    
    #
    # PRIVATE METHODS
    #
    
