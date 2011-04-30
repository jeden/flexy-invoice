#
# Exceptions
#

class DuplicatedEntityException(Exception):
    """  Thrown when a field uniqueness constraint is violated """
    def __init__(self, model, field_name, field_value):
        Exception.__init__(self, "Uniqueness constraint violated: model = %s, field name = %s, field value = %s" % (model, field_name, field_value))

#
# Model utilities
#

def check_for_uniqueness(model, field_name, field_value):
    """
    Verify uniqueness of the specified pair (field, value)

    Parameters:
    - model: the model class
    - field_name: name of the field
    - field_value: the field value to be checked for uniqueness

    Throw a DuplicatedEntityException if the specified value
    is already used
    """

    query = model.all(keys_only = True).filter(field_name, field_value)
    entity = query.get()
    if entity:
        raise DuplicatedEntityException(model, field_name, field_value)

    