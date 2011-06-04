'''
Created on Apr 26, 2011

@author: Antonio Bello
'''
from test.test_base_appengine_datastore_tester import BaseAppengineDatastoreTester
from logic.invoice_manager import InvoiceManager
from model.invoice_models import InvoiceEntity, InvoiceItemEntity
from test import helpers
from datetime import date

class Test_Invoice_Manager(BaseAppengineDatastoreTester):
    """ Test invoice creation """
        
    def setUp(self):
        super(Test_Invoice_Manager, self).setUp()
        
        self._test_user = helpers.create_dummy_user(1)
        self._test_currency = helpers.create_dummy_currency(1)
        self._test_client = helpers.create_dummy_client(1, self._test_user, currency = self._test_currency)
        self._invoice_manager = InvoiceManager(self._test_user)

    def test_create_invoice(self):
        ''' Create a new invoice, add 2 invoice items and save '''
        self._invoice_manager.create(
                                     client_id = self._test_client.key().id(),
                                     invoice_no = '01/2011',
                                     invoice_date = date.today(),
                                     sale_date = date.today(),
                                     currency_id = self._test_currency.key().id()
                                )
        self._invoice_manager.add_invoice_item(description = 'sample item1', quantity = 1.0, unit_price = 10.0)
        self._invoice_manager.add_invoice_item(description = 'sample item2', quantity = 2.0, unit_price = 15.0)
        
        # Save the invoice
        self._invoice_manager.save()
        
        # Verify the instance is an invoice
        invoice = self._invoice_manager.invoice
        self.verify_entity_instance(invoice, InvoiceEntity)
        self.assertEqual(len(invoice.invoice_items.fetch(1000)), 2)
        
        # Verify invoice detail instances
        invoice_items = self._invoice_manager.invoice_items
        
        for item in invoice_items:
            self.verify_entity_instance(item, InvoiceItemEntity)
            self.assertEqual(item.invoice.key(), invoice.key())
            self.assertEqual(item.parent.key(), invoice.key())
        
        # Check totals
        self.assertEqual(invoice_items[0].total, 10.0)
        self.assertEqual(invoice_items[1].total, 30.0)

        self.assertEqual(invoice.subtotal, 40.0)
        self.assertEqual(invoice.total, 40.0)
