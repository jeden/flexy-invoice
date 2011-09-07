'''
Created on Jun 1, 2011

@author: Antonio Bello - Elapsus
'''
from model.user_models import UserAccountType
from logic.client_manager import ClientManager
from logic.currency_manager import CurrencyManager
from logic.user_manager import UserManager
from google.appengine.api import users
from logic.language_manager import LanguageManager

'''
def create_dummy_invoice(user, index, invoice_manager = None):
    """
        Create a dummy invoice
        
        PARAMETERS:
        - user creating the invoice
        - index: number to uniquely identify the invoice
        - invoice_manager: the invoice manager - if none is provided, a new one is created
    """
    if invoice_manager == None:
        invoice_manager = InvoiceManager()
    
    return invoice_manager.create_invoice(user)

def create_dummy_invoice_item(invoice, index, count = 1, invoice_manager = None):
    """
    Create a dummy invoice item
    
    PARAMETERS:
    - invoice: the invoice the item has to be added to
    - index: number to uniquely identify the invoice item
    - the number of invoice items to add
        - invoice_manager: the invoice manager - if none is provided, a new one is created
    """
    
    if invoice_manager == None:
        invoice_manager = InvoiceManager()
    
    if count == 1:
        ret = invoice_manager.add_invoice_item(
            invoice = invoice,
            description = 'description %i' % index,
            quantity = index,
            price = index * 13.0
        )
    else:
        ret = ()
        for i in range (0, count):
            ret.append(
                invoice_manager.add_invoice_item(
                    invoice = invoice,
                    description = 'description %i' % i,
                    quantity = i,
                    price = i * 13.0
                )
            )
    return ret
'''
def create_dummy_client(index, user, client_manager = None, language = None, currency = None):
    """ Create a dummy client """
    
    if client_manager == None:
        client_manager = ClientManager(user.user)
    
    if currency is None:
        currency = create_dummy_currency(index)
        
    if language is None:
        language = create_dummy_language(index)
    
    return client_manager.add_client(
        name = 'client_%i' %index,
        address = 'address_%i' % index,
        email = 'corp_email_%i@email.com' % index,
        default_currency_id = currency.key().id(),
        default_language_id = language.key().id(),
    )

def add_dummy_contact(index, client, user, client_manager = None):
    """ add a dummy client contact """

    if client_manager == None:
        client_manager = ClientManager(user.user)

    return client_manager.add_client_contact(
        client = client, 
        name = 'name_%i' % index,
        email = 'email%i@email.com' % index
    )

def create_dummy_currency(index, currency_manager = None):
    if currency_manager == None:
        currency_manager = CurrencyManager()
        
    return currency_manager.create_currency(
        name = 'US%i Dollar' % index,
        code = 'USD%i' % index,
        symbol = '$%i'  % index
    )
    
def create_dummy_user(index, account_type = UserAccountType.FREE, user_manager = None):
    if user_manager == None:
        user_manager = UserManager()
        
    return user_manager.register_user(
        google_account = users.User('email_%i@gmail.com' % index),
        account_type = account_type
    )

def create_dummy_language(index):
    return LanguageManager.create_language(name = 'language_%i' % index)