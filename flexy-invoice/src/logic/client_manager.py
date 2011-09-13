'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from model.client_models import ClientEntity, ClientContactEntity
from google.appengine.ext import db

class ClientManager:
    __QUERY_LIST_CLIENT = db.GqlQuery('SELECT * FROM ClientEntity WHERE user = :user ORDER BY name')
    
    def __init__(self, user):
        self._user = user
         
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
        
    def listify_clients(self):
        '''
            Return the list of user clients, formatted to be used in a listbox 
            as a list of tuples (id, name)
            An element representing no selection is added at top
        '''
        list = [(client.key().id(), client.name) for client in self.list_clients()]
        list.insert(0, ('', ''))
        return list 

        
    def list_clients(self, start_from = 0, size = 10000):
        """
            Return the list of clients 
        """
        self.__QUERY_LIST_CLIENT.bind(user = self._user)
        return self.__QUERY_LIST_CLIENT.fetch(size, start_from)
    
    @classmethod
    def find_by_id(cls, client_id):
        ''' Find a client by his key id '''
        return ClientEntity.get_by_id(client_id)