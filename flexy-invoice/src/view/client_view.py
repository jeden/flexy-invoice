'''
Created on May 21, 2011

@author: Antonio Bello - Elapsus
'''
from google.appengine.ext.db import djangoforms
from django import forms 
from logic.currency_manager import CurrencyManager
from logic.client_manager import ClientManager
from logic.language_manager import LanguageManager
from view import EmailInput, TextInput, Textarea, Select
from flexy.web.handler.base_handler import BaseProtectedHandler
from flexy.utils.rendering import render_template
from flexy.web.handler.command_base import CommandBase
from flexy.web.handler.async_handler import AsyncHandler

class ClientForm(djangoforms.ModelForm):
    """ Form for creating and editing a client """
    name = forms.CharField(label = 'Name')
    address = forms.CharField(label = 'Address')
    email = forms.EmailField(label = 'Email')
    default_currency = forms.ChoiceField(label = 'Default Currency')
    default_language = forms.ChoiceField(label = "Default Language")
    
    name.widget = TextInput(placeholder = 'Client name')
    address.widget = Textarea(cols = 30, rows = 5, placeholder = 'Client address')
    email.widget = EmailInput(placeholder = 'Client email address')
    default_currency.widget = Select()
    default_language.widget = Select()
    
    
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        # Initialize the currencies drop down        
        currencies = CurrencyManager.list_currencies()
        currencies.insert(0, ('', ''))
        self.fields['default_currency'].choices = currencies
        
        # Initialize the languages drop down
        languages = LanguageManager.list_languages()
        languages.insert(0, ('', ''))
        self.fields['default_language'].choices = languages
        
        self.prefix = 'client'
        self.auto_id = '%s'
        
class AddClientHandler(BaseProtectedHandler):
    """ Handler to add a new client """

    def get(self, form = ClientForm()):
        return render_template(self, 'client_add.html', {
                                                       'form': form
                                                       })
    
    def post(self):
        form = ClientForm(data = self.request.POST)
        if form.is_valid():
            client_manager = ClientManager(self._user_session.get_user())
            
            name = form['name'].data
            address = form['address'].data
            email = form['email'].data
            default_currency_id = form['default_currency'].data
            default_language_id = form['default_language'].data

            client_manager.add_client(name, address, email, default_currency_id, default_language_id)
        else:
            self.get(form)
            
class ListClientsHandler(BaseProtectedHandler):
    def get(self):
        return render_template(self, 'client_list.html')

class ClientListCommand(CommandBase):
    """
        Async command to retrieve clients in json format
    """
    def _execute(self):
        client_manager = ClientManager(self._user_session.get_user())
        clients = client_manager.list_clients()
        json = self.jsonize_jqgrid(clients)
        return self.render_content(json) 
                
class ClientAsync(AsyncHandler):
    """
        Async handler to retrieve clients
    """
    routing_table = {
                     'list': [ClientListCommand, {}]
                     }
    
    def _get_routing_table(self):
        return ClientAsync.routing_table

