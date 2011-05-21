'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from test.test_base_appengine_datastore_tester import BaseAppengineDatastoreTester
from logic.client_manager import ClientManager
from model.client_models import ClientEntity, ClientContactEntity
from test.test_user import Test_User_Manager
from model.domain_models import CurrencyEntity
from test.test_currency import Test_Currency


class TestClientManager(BaseAppengineDatastoreTester):
    """ Client manager tests """
    
    client_manager = ClientManager()
    test_user = None
    
    def setUp(self):
        BaseAppengineDatastoreTester.setUp(self)
        self.test_user = Test_User_Manager.create_dummy_user()
    
    def test_create_client(self):
        """ Test the creation of a new client """
        client = self.__create_dummy_client(1)
        self.verify_entity_instance(client, ClientEntity)
        self.verify_entity_instance(client.default_currency, CurrencyEntity)
        
    def test_add_client_contact(self):
        client = self.__create_dummy_client(1)
        contact = self.__add_dummy_contact(client, 1)
        self.verify_entity_instance(contact, ClientContactEntity)
        
    ###
    ### PRIVATE METHODS
    ###
    
    def __create_dummy_client(self, index):
        """ Create a dummy client """
        currency = Test_Currency.create_dummy_currency(index)
        
        return self.client_manager.add_client(
            name = 'client_%i' %index,
            address = 'address_%i' % index,
            email = 'corp_email_%i@email.com' % index,
            default_currency = currency,
            user = self.test_user
        )
    
    def __add_dummy_contact(self, client, index):
        """ add a dummy client contact """
        return self.client_manager.add_client_contact(
            client = client, 
            name = 'name_%i' % index,
            email = 'email%i@email.com' % index
        )
    