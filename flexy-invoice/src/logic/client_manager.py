'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from model.client_models import ClientEntity, ClientContactEntity

class ClientManager:
    def add_client(self, user, name, address, email, default_currency):
        """ Create a new client """
        client = ClientEntity.create(user = user, name = name, address = address, email = email, default_currency = default_currency)
        client.put()
        return client
    
    def add_client_contact(self, client, name, email):
        contact = ClientContactEntity.create(client = client, name = name, email = email)
        contact.put()
        return contact
        