'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from model.invoice_models import InvoiceEntity, InvoiceItemEntity
from logic.client_manager import ClientManager
from logic.currency_manager import CurrencyManager
from google.appengine.ext import db
from logic.language_manager import LanguageManager

class InvoiceException(Exception):
    pass

class InvoiceManager:
    """ Invoice creation and management """
    
    __QUERY_LIST_INVOICES = db.GqlQuery('SELECT * FROM InvoiceEntity WHERE user = :user ORDER BY invoice_date DESC')
    
    def __init__(self, user):
        self._user = user
        self._invoice = None
        self._invoice_items = []
    
    def create(self, client_id, invoice_no, invoice_date, sale_date, currency_id = None, language_id = None):
        '''
            Create a new invoice
        '''
        self._invoice_items = []
        
        client = ClientManager.find_by_id(client_id)
        
        if currency_id is None:
            currency = client.default_currency
        else:
            currency = CurrencyManager.find_by_id(currency_id)
        
        if language_id is None:
            language = client.default_language
        else:
            language = LanguageManager.find_by_id(language_id)
        
        self._invoice = InvoiceEntity.create(
                                       user = self._user,
                                       client = client,
                                       currency = currency,
                                       language = language,
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
        ''' 
        Save the invoice along with its invoice items
        If no invoice item has been provided, an InvoiceException is raised 
        '''

        if not self._invoice_items:
            raise InvoiceException();        
        
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

    def list_invoices(self, start_from = 0, size = 10000):
        """
            Return the list of invoices 
        """
        self.__QUERY_LIST_INVOICES.bind(user = self._user)
        return self.__QUERY_LIST_INVOICES.fetch(size, start_from)

    def find_invoice_by_id(self, invoice_id):
        """ Find an invoice entity by its id """
        invoice = InvoiceEntity.get_by_id(invoice_id)
        if invoice is not None:
            # If the invoice belongs to another user, set the result to None
            if invoice.user.key() != self._user.key():
                invoice = None
    
        return invoice
    
    #
    # PRIVATE METHODS
    #
    
