'''
Created on Jun 2, 2011

@author: Antonio Bello - Elapsus
'''
from django import forms
from util.base_handler import BaseProtectedHandler
from util import render_template
from logic.client_manager import ClientManager
from google.appengine.api.users import get_current_user
from logic.currency_manager import CurrencyManager
from logic.invoice_manager import InvoiceManager
import datetime
from util.dojifier import dojify_form, DojoType, DojoControlType

class InvoiceForm(forms.Form):
    client = forms.TypedChoiceField(label = 'Client', coerce = int, empty_value = None) 
    currency = forms.TypedChoiceField(label = 'Currency', coerce = int, empty_value = None)
    invoice_no = forms.CharField(label="Invoice #")
    invoice_date = forms.DateField(label = "Invoice Date", input_formats = ['%Y-%m-%d'])
    sale_date = forms.DateField(label = "Sale Date", input_formats = ['%Y-%m-%d'])
    items = forms.IntegerField(widget = forms.HiddenInput)

    dojify_form ([
                  DojoType(client, forms.Select, DojoControlType.Select, True),
                  DojoType(currency, forms.Select, DojoControlType.Select, True),
                  DojoType(invoice_no, forms.TextInput, DojoControlType.ValidationTextBox, True),
                  DojoType(invoice_date, forms.DateInput, DojoControlType.DateTextBox, True, {'datePattern': 'yyyy-MM-dd'}),
                  DojoType(sale_date, forms.DateInput, DojoControlType.DateTextBox, True, {'datePattern': 'yyyy-MM-dd'}),
                  ])
    

    def __init__(self, invoice_items = 1, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        
        user = get_current_user()
        client_manager = ClientManager(user)
        
        # Initialize the client drop down
        clients = client_manager.list_clients()
        clients.insert(0, ('', ''))
        self.fields['client'].choices = clients
        
        #Initialize the currencies drop down
        currencies = CurrencyManager.list_currencies()
        currencies.insert(0, ('', ''))
        self.fields['currency'].choices = currencies
        
        self.fields['items'].initial = invoice_items
        
        # Initialize invoice and sale date to today
        self.fields['invoice_date'].initial = datetime.date.today() 
        self.fields['sale_date'].initial = datetime.date.today()
        
        self.prefix = 'invoice'
        self.auto_id = '%s'

class InvoiceItemForm(forms.Form):
    description = forms.CharField(label = 'Description')
    unit_price = forms.FloatField(label = 'Unit price')
    quantity = forms.FloatField(label = 'Quantity')

    dojify_form([
                 DojoType(description, forms.TextInput, DojoControlType.ValidationTextBox, True),
                 DojoType(unit_price, forms.TextInput, DojoControlType.CurrencyTextBox, True),
                 DojoType(quantity, forms.TextInput, DojoControlType.NumberSpinner, True)
    ])

    def __init__(self, index, *args, **kwargs):
        super(InvoiceItemForm, self).__init__(*args, **kwargs)
        self.prefix = '%i_invoice_item' % index
        self.auto_id = '%s'
        
class CreateInvoiceHandler(BaseProtectedHandler):
    ''' Create a new invoice '''
    
    def get(self, invoice_form = InvoiceForm(), invoice_item_forms = [InvoiceItemForm(index = 1)]):
        
        return render_template(self, 'invoice_create.html', {
                                                       'invoice_form': invoice_form,
                                                       'invoice_item_forms': invoice_item_forms,
                                                       })
    def post(self):
        commit = False
        
        invoice_manager = InvoiceManager(self._user_session.get_user())
        
        invoice_form = InvoiceForm(data = self.request.POST)
        items = invoice_form.fields['items'].to_python(self.request.POST['invoice-items']) or 0
        invoice_item_forms = [InvoiceItemForm(index + 1, self.request.POST) for index in range(0, items)]
        
        if invoice_form.is_valid():
            # Validates the invoice items
            commit = True
            for form in invoice_item_forms:
                if not form.is_valid():
                    commit = False
                    break

        if commit:
            invoice_manager.create(
                                   client_id = invoice_form.cleaned_data['client'],
                                   currency_id = invoice_form.cleaned_data['currency'],
                                   invoice_no = invoice_form.cleaned_data['invoice_no'],
                                   invoice_date = invoice_form.cleaned_data['invoice_date'],
                                   sale_date = invoice_form.cleaned_data['sale_date']
                                )
            for invoice_item in invoice_item_forms:
                invoice_manager.add_invoice_item(
                                                 description = invoice_item.cleaned_data['description'], 
                                                 quantity = invoice_item.cleaned_data['quantity'], 
                                                 unit_price = invoice_item.cleaned_data['unit_price']
                                            )
                
            invoice_manager.save()
        else:
            self.get(invoice_form, invoice_item_forms)
