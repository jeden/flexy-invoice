'''
Created on Apr 27, 2011

@author: Antonio Bello - Elapsus
'''
from model.invoice_models import CurrencyEntity, ExchangeRateEntity
from google.appengine.ext import db
from model.model_utils import DuplicatedEntityException

class CurrencyException(Exception):
    pass

class CurrencyManager:
    def create_currency(self, name, symbol):
        """ Create a new currency """
        try:
            currency = CurrencyEntity.create(name = name, symbol = symbol)
            currency.put()
        except(DuplicatedEntityException):
            raise CurrencyException
        
        return currency
    
    def add_exchange_rate(self, from_currency, to_currency, date, rate):
        """ Add a conversion rate from one currency to another at the specified day """
        exchange_rate = self.__get_exchange_rate(from_currency, to_currency, date)
        if (exchange_rate is not None):
            raise CurrencyException()
        
        if from_currency == to_currency:
            raise CurrencyException

        exchange_rate = ExchangeRateEntity.create(from_currency, to_currency, date, rate)
        exchange_rate.put()
    
    def convert_currency(self, from_currency, to_currency, date, amount):
        """ Convert the from currency to the to currency using the rage of the specified date """
        exchange_rate = self.__get_exchange_rate(from_currency, to_currency, date)

        if exchange_rate is None:
            raise CurrencyException
    
        return exchange_rate.rate * amount

    def __get_exchange_rate(self, from_currency, to_currency, date):
        """ Find the exchange rate for the specified pair of currencies and date """
        query = db.Query(ExchangeRateEntity)
        query.filter('from_currency = ', from_currency)
        query.filter('to_currency = ', to_currency)
        query.filter('date = ', date)
        return query.get()
        
