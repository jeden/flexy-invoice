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
from logic.language_manager import LanguageManager
from util.dojifier import dojify_form, DojoType, DojoControlType

class ClientForm(djangoforms.ModelForm):
    """ Form for creating and editing a client """
    name = forms.CharField(label = 'Name')
    address = forms.CharField(label = 'Address', widget = forms.Textarea(attrs={'cols': 30, 'rows': 5}))
    email = forms.EmailField(label = 'Email')
    default_currency = forms.ChoiceField(label = 'Default Currency')
    default_language = forms.ChoiceField(label = "Default Language")
    
    dojify_form([
            DojoType(field = name, dojo_type = DojoControlType.ValidationTextBox, required = True),
            DojoType(field = address, dojo_type = DojoControlType.Textarea, required = True),
            DojoType(field = email, dojo_type = DojoControlType.ValidationTextBox, required = True, attributes = {'regExp': '[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'}),
            DojoType(field = default_currency, dojo_type = DojoControlType.Select, required = True),
            DojoType(field = default_language, dojo_type = DojoControlType.Select, required = True)            
    ])
    
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
            user = users.get_current_user()
            name = form['name'].data
            address = form['address'].data
            email = form['email'].data
            default_currency_id = form['default_currency'].data
            default_language_id = form['default_language'].data

            ClientManager.add_client(user, name, address, email, default_currency_id, default_language_id)
        else:
            self.get(form)
