'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from model.client_models import ClientEntity, ClientContactEntity
from logic.user_manager import UserManager
from google.appengine.ext import db

class ClientManager:
    __QUERY_LIST_CLIENT = db.GqlQuery('SELECT * FROM ClientEntity WHERE user = :user ORDER BY name')
    
    def __init__(self, account):
        self._user = UserManager.retrieve_user_by_account(account)
         
    def add_client(self, name, address, email, default_currency_id, default_language_id):
        """ Create a new client """
        currency_key = db.Key.from_path('CurrencyEntity', int(default_currency_id))
        language_key = db.Key.from_path('LanguageEntity', int(default_language_id))
        client = ClientEntity.create(user = self._user, name = name, address = address, email = email, default_currency = currency_key, default_language = language_key)
        client.put()
        return client
    
    def add_client_contact(self, client, name, email):
        contact = ClientContactEntity.create(client = client, name = name, email = email)
        contact.put()
        return contact
        
    def list_clients(self):
        '''
            Return the list of user clients, formatted to be used in a listbox 
            as a list of tuples (id, name)
        '''
        self.__QUERY_LIST_CLIENT.bind(user = self._user)
        clients = self.__QUERY_LIST_CLIENT.run()
        list = [(client.key().id(), client.name) for client in clients]
        
        return list
    
    @classmethod
    def find_by_id(cls, client_id):
        ''' Find a client by his key id '''
        return ClientEntity.get_by_id(client_id)