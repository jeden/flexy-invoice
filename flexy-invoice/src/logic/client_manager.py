'''
Created on Apr 26, 2011

@author: Antonio Bello - Elapsus
'''
from model.client_models import ClientEntity, ClientContactEntity
from logic.user_manager import UserManager
from google.appengine.ext import db

class ClientManager:
    @classmethod
    def add_client(self, account, name, address, email, default_currency_id):
        """ Create a new client """
        user = UserManager.retrieve_user_by_account(account)
        currency_key = db.Key.from_path('CurrencyEntity', default_currency_id)
        client = ClientEntity.create(user = user, name = name, address = address, email = email, default_currency = currency_key)
        client.put()
        return client
    
    def add_client_contact(self, client, name, email):
        contact = ClientContactEntity.create(client = client, name = name, email = email)
        contact.put()
        return contact
        