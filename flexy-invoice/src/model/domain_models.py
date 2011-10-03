'''
Created on Apr 30, 2011

@author: Antonio Bello - Elapsus
'''
from google.appengine.ext import db
from flexy.model.db_model import DbModel

class CurrencyEntity(DbModel):
    """ Currency entity """
    
    name = db.StringProperty(required = True)
    code = db.StringProperty(required = True)
    symbol = db.StringProperty(required = True)
    
    @classmethod
    def create(cls, name, code, symbol):
        cls.check_for_uniqueness('code', code)
        return cls(name = name, symbol = symbol, code = code)
    
class ExchangeRateEntity(DbModel):
    """ Exchange rate between two currencies """
    from_currency = db.ReferenceProperty(reference_class = CurrencyEntity, required = True, collection_name = "to_currencies")
    to_currency = db.ReferenceProperty(reference_class = CurrencyEntity, required = True, collection_name = "from_currencies")
    date = db.DateProperty(required = True)
    rate = db.FloatProperty(required = True)
    
    @classmethod
    def create(cls, from_currency, to_currency, date, rate):
        """ Create a new exchange rate instance """
        return cls(from_currency = from_currency, to_currency = to_currency, date = date, rate = rate)
    
class LanguageEntity(DbModel):
    """ Language entity """
    
    name = db.StringProperty(required = True)
    
    @classmethod
    def create(cls, name):
        cls.check_for_uniqueness('name', name)
        return cls(name = name)
    