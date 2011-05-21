'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from model.invoice_models import InvoiceEntity, InvoiceItemEntity

class InvoiceManager:
    """ Invoice creation and management """
    
    def create_invoice(self, user):
        invoice = InvoiceEntity.create(user = user)
        invoice.put()
        return invoice
    
    def add_invoice_item(self, invoice, description, quantity, price):
        invoice_item = InvoiceItemEntity.create(invoice = invoice, description = description, quantity = quantity, price = price)
        invoice_item.put()
        return invoice_item
