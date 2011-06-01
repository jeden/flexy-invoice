'''
Created on Apr 26, 2011

@author: Antonio Bello
'''
from test.test_base_appengine_datastore_tester import BaseAppengineDatastoreTester
from logic.invoice_manager import InvoiceManager
from model.invoice_models import InvoiceEntity, InvoiceItemEntity
from test.test_user import Test_User_Manager

class Test_Invoice_Manager(BaseAppengineDatastoreTester):
    """ Test invoice creation """
        
    invoice_manager = InvoiceManager()
    test_user = None

    def setUp(self):
        BaseAppengineDatastoreTester.setUp(self)
        self.test_user = Test_User_Manager.create_dummy_user()

    def test_create_invoice(self):
        invoice = self.__create_dummy_invoice(self.test_user, 1)
        self.verify_entity_instance(invoice, InvoiceEntity)
        
        invoice_item = self.__create_dummy_invoice_item(invoice, 1)
        self.verify_entity_instance(invoice_item, InvoiceItemEntity)
        
    ###
    ### PRIVATE METHODS
    ###
    
    def __create_dummy_invoice(self, user, index):
        """
            Create a dummy invoice
            
            PARAMETERS:
            - user creating the invoice
            - index: number to uniquely identify the invoice
        """
        return self.invoice_manager.create_invoice(user)
    
    def __create_dummy_invoice_item(self, invoice, index, count = 1):
        """
        Create a dummy invoice item
        
        PARAMETERS:
        - invoice: the invoice the item has to be added to
        - index: number to uniquely identify the invoice item
        - the number of invoice items to add
        """
        
        if count == 1:
            ret = self.invoice_manager.add_invoice_item(
                invoice = invoice,
                description = 'description %i' % index,
                quantity = index,
                price = index * 13.0
            )
        else:
            ret = ()
            for i in range (0, count):
                ret.append(
                    self.invoice_manager.add_invoice_item(
                        invoice = invoice,
                        description = 'description %i' % i,
                        quantity = i,
                        price = i * 13.0
                    )
                )
        return ret