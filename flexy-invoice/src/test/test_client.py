'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from test.test_base_appengine_datastore_tester import BaseAppengineDatastoreTester
from logic.client_manager import ClientManager
from model.client_models import ClientEntity, ClientContactEntity
from model.domain_models import CurrencyEntity, LanguageEntity
from test import helpers
from test.helpers import create_dummy_client
from model.user_models import UserEntity


class TestClientManager(BaseAppengineDatastoreTester):
    """ Client manager tests """
    
    def setUp(self):
        super(TestClientManager, self).setUp()
        self.test_user = helpers.create_dummy_user(1)
        self.verify_entity_instance(self.test_user, UserEntity)
        self.client_manager = ClientManager(self.test_user.user)
    
    def test_create_client(self):
        """ Test the creation of a new client """
        client = helpers.create_dummy_client(1, self.test_user)
        self.verify_entity_instance(client, ClientEntity)
        self.verify_entity_instance(client.default_currency, CurrencyEntity)
        self.verify_entity_instance(client.default_language, LanguageEntity)
        
        # Verify the client is private to the user
        self.assertEqual(client.user.key(), self.test_user.key())
        
    def test_add_client_contact(self):
        client = helpers.create_dummy_client(1, self.test_user)
        contact = helpers.add_dummy_contact(1, client, self.test_user)
        self.verify_entity_instance(contact, ClientContactEntity)
    
    def test_list_contacts(self):
        ''' 
            Verify that the list contacts method returns the list of the user clients
            as a list of (id, contact) tuples
        
         '''
        user1 = helpers.create_dummy_user(11)
        user2 = helpers.create_dummy_user(12)
        
        create_dummy_client(1, user1)
        create_dummy_client(2, user2)
        create_dummy_client(3, user1)
        create_dummy_client(4, user2)
        create_dummy_client(5, user1)
        create_dummy_client(6, user2)
        create_dummy_client(7, user1)
         
        client_manager_1 = ClientManager(user1)
        client_manager_2 = ClientManager(user2)
         
        clients_1 = client_manager_1.list_clients()
        clients_2 = client_manager_2.list_clients()
         
        self.assertEqual(len(clients_1), 4)
        self.assertEqual(len(clients_2), 3)
        