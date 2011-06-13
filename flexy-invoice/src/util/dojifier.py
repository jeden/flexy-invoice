'''
Created on Jun 5, 2011

@author: Antonio Bello - Elapsus
'''

from util.Enum import Enum

DojoControlType = Enum([ 'Select', 'Button', 'TextBox', 'ValidationTextBox', 'DateTextBox', 'CurrencyTextBox', 'NumberSpinner', 'Textarea'])

def dojify_control(field, dojo_type, required = False, attributes = {}):
    ''' 
        Apply a dojo type to a django form field.
        Args:
        * field: the form field to change
        * dojo_type: the dojo type, selectable from the DojoControlType enum
        * required: boolean indicating whether to apply the required attribute to the html control
    ''' 
    
    field.widget.attrs.update(dict({ 'dojoType': 'dijit.form.%s' % dojo_type, 'required': required and 'true' or 'false' }, **attributes))

def dojify_form(field_definitions):
    '''
        Apply a dojo type to each of the specified django form fields
        Args:
        * field definition: list of DojoType instances
    '''
    for field_definition in field_definitions:
        dojify_control(field_definition.field, field_definition.dojo_type, field_definition.required, field_definition.attributes)
        
class DojoType:
    def __init__(self, field, dojo_type, required = False, attributes = {}, style = {}, style_class = [], constraints = {}):
        self.field = field
        self.dojo_type = dojo_type
        self.required = required
        self.attributes = attributes.copy()

        if style:
            self.attributes['style'] = '; '.join('%s: %s' % (key, value) for key, value in style.items())

        if style_class:
            self.attributes['class'] = ' '.join(value for value in style_class)

        if constraints:
            self.attributes['constraints'] = "; ".join("{%s: '%s'}"% (key, value) for key, value in constraints.items())