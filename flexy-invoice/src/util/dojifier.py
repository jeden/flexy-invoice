'''
Created on Jun 5, 2011

@author: Antonio Bello - Elapsus
'''
from util.Enum import Enum

DojoControlType = Enum([ 'Select', 'Button', 'TextBox', 'ValidationTextBox', 'DateTextBox', 'CurrencyTextBox', 'NumberSpinner'])

def dojify_control(field, widget, dojo_type, required = False, attributes = {}):
    ''' 
        Apply a dojo type to a django form field.
        Args:
        * field: the form field to change
        * widget: the widget class type to use for the field
        * dojo_type: the dojo type, selectable from the DojoControlType enum
        * required: boolean indicating whether to apply the required attribute to the html control
    ''' 
    
    field.widget = widget(attrs = dict({ 'dojoType': 'dijit.form.%s' % dojo_type, 'required': required }, **attributes))

def dojify_form(field_definitions):
    '''
        Apply a dojo type to each of the specified django form fields
        Args:
        * field definition: list of DojoType instances
    '''
    for field_definition in field_definitions:
        dojify_control(field_definition.field, field_definition.widget, field_definition.dojo_type, field_definition.required, field_definition.attributes)
        
class DojoType:
    def __init__(self, field, widget, dojo_type, required = False, attributes = {}):
        self.field = field
        self.widget = widget
        self.dojo_type = dojo_type,
        self.required = required,
        self.attributes = attributes
