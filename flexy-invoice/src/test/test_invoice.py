'''
Created on Apr 26, 2011

@author: Antonio Bello
'''
from test.test_base_appengine_datastore_tester import BaseAppengineDatastoreTester
from logic.invoice_manager import InvoiceManager
from model.invoice_models import InvoiceEntity

class Test_Invoice_Manager(BaseAppengineDatastoreTester):
    """ Test invoice creation """
        
    invoice_manager = InvoiceManager()

    def test_create_invoice(self):
        invoice = self.__create_dummy_invoice(1)
        self.assertIsNotNone(invoice)
        self.assertIsInstance(invoice, InvoiceEntity)
        
        invoice_item = self.__create_dummy_invoice_item(invoice, 1)
        #self.assertIsNotNone(invoice_item)
        #self.assertIsInstance(invoice_item, InvoiceItemEntity)

        
    ###
    ### PRIVATE METHODS
    ###
    
    def __create_dummy_invoice(self, index):
        """
            Create a dummy invoice
            
            PARAMETERS:
            - index: number to uniquely identify the invoice
        """
        return InvoiceEntity()
    
    def __create_dummy_invoice_item(self, invoice, index):
        """
        Create a dummy invoice item
        
        PARAMETERS:
        - invoice: the invoice the item has to be added to
        - index: number to uniquely identify the invoice item
        """
        #self.invoice_manager.add_invoice_item()