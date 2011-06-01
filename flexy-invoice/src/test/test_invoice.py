'''
Created on Apr 26, 2011

@author: Antonio Bello
'''
from test.test_base_appengine_datastore_tester import BaseAppengineDatastoreTester
from logic.invoice_manager import InvoiceManager
from model.invoice_models import InvoiceEntity, InvoiceItemEntity
from test.helpers import create_dummy_user
from test import helpers

class Test_Invoice_Manager(BaseAppengineDatastoreTester):
    """ Test invoice creation """
        
    def setUp(self):
        super(Test_Invoice_Manager, self).setUp()
        
        self._invoice_manager = InvoiceManager()
        self._test_user = create_dummy_user(1)

    def test_create_invoice(self):
        invoice = helpers.create_dummy_invoice(self._test_user, 1)
        self.verify_entity_instance(invoice, InvoiceEntity)
        
        invoice_item = helpers.create_dummy_invoice_item(invoice, 1)
        self.verify_entity_instance(invoice_item, InvoiceItemEntity)
        
