'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from test.test_base_appengine_datastore_tester import BaseAppengineDatastoreTester
from logic.client_manager import ClientManager
from model.client_models import ClientEntity, ClientContactEntity
from model.domain_models import CurrencyEntity, LanguageEntity
from test import helpers


class TestClientManager(BaseAppengineDatastoreTester):
    """ Client manager tests """
    
    def setUp(self):
        super(TestClientManager, self).setUp()
        self.client_manager = ClientManager()
        self.test_user = helpers.create_dummy_user(1)
    
    def test_create_client(self):
        """ Test the creation of a new client """
        client = helpers.create_dummy_client(1, self.test_user)
        self.verify_entity_instance(client, ClientEntity)
        self.verify_entity_instance(client.default_currency, CurrencyEntity)
        self.verify_entity_instance(client.default_language, LanguageEntity)
        
    def test_add_client_contact(self):
        client = helpers.create_dummy_client(1, self.test_user)
        contact = helpers.add_dummy_contact(client, 1)
        self.verify_entity_instance(contact, ClientContactEntity)
    