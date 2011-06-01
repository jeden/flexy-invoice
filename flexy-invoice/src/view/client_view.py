'''
Created on May 21, 2011

@author: Antonio Bello - Elapsus
'''
from google.appengine.ext.db import djangoforms
from util import render_template
from django import forms 
from logic.currency_manager import CurrencyManager
from logic.client_manager import ClientManager
from google.appengine.api import users
from util.base_handler import BaseProtectedHandler

class ClientForm(djangoforms.ModelForm):
    """ Form for creating and editing a client """
    name = forms.CharField(label = 'Name')
    address = forms.CharField(label = 'Address', widget = forms.Textarea(attrs={'cols': 30, 'rows': 5}))
    email = forms.EmailField(label = 'Email')
    default_currency = forms.ChoiceField(label = 'Default Currency')
    
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        
        currencies = CurrencyManager.get_currencies_list()
        currencies.insert(0, ('', '--Select--'))
        self.fields['default_currency'].choices = currencies
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
            user = users.get_current_user()
            name = form['name'].data
            address = form['address'].data
            email = form['email'].data
            default_currency_id = form['default_currency'].data

            ClientManager.add_client(user, name, address, email, default_currency_id)
        else:
            self.get(form)
