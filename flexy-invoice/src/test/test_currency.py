'''
Created on Apr 27, 2011

@author: Antonio Bello - Elapsus
'''
from test.test_base_appengine_datastore_tester import BaseAppengineDatastoreTester
from datetime import date
from logic.currency_manager import CurrencyManager, CurrencyException
from model.domain_models import CurrencyEntity
from test import helpers

class Test_Currency(BaseAppengineDatastoreTester):
    """  Currency management tests """
    
    def setUp(self):
        super(Test_Currency, self).setUp()
        self.entity_manager = CurrencyManager()
    
    def test_create_currency(self):
        """ Test adding a currency """
        currency = helpers.create_dummy_currency(1)
        self.verify_entity_instance(currency, CurrencyEntity)
    
    def test_create_existing_currency(self):
        """ Verify that adding a currency with an already existing symbol generates an exception """
        currency = helpers.create_dummy_currency(1)
        try:
            currency = helpers.create_dummy_currency(1)
            self.fail('Added a duplicated currency symbol')
        except(CurrencyException):
            pass
    
    def test_add_exchange_rate_and_verify_conversion(self):
        """ Add an exchange rate from currency 1 to currency 2 and verify conversion occurs """
        currency1 = helpers.create_dummy_currency(1)
        currency2 = helpers.create_dummy_currency(2)
        self.entity_manager.add_exchange_rate(from_currency = currency1, to_currency = currency2, date = date.today(), rate = 1.2)
        
        value1 = 10.0
        value2 = self.entity_manager.convert_currency(from_currency = currency1, to_currency = currency2, date = date.today(), amount = value1)
        self.assertEqual(value2, 12.0)
    
    def test_exchange_rate_on_missing_day(self):
        """ Verify that a conversion using the rate of a day not inserted in the database generates an exception """
        currency1 = helpers.create_dummy_currency(1)
        currency2 = helpers.create_dummy_currency(2)
        value1 = 10.0
        
        try:
            self.entity_manager.convert_currency(from_currency = currency1, to_currency = currency2, date = date.today(), amount = value1)
            self.fail('Conversion occurred!!')
        except(CurrencyException):
            pass
    
    def test_exchange_rate_for_one_currency(self):
        """ Verify that an exchange rate cannot be created if the from and to currency are the same """
        currency1 = helpers.create_dummy_currency(1)
        try:
            self.entity_manager.add_exchange_rate(from_currency = currency1, to_currency = currency1, date = date.today(), rate = 1.2)
            self.fail('Added a conversion rate from and to the same currency')
        except(CurrencyException):
            pass

    def test_duplicated_exchange_rate(self):
        """ Verify that a conversion rate cannot be added twice for the same day """
        currency1 = helpers.create_dummy_currency(1)
        currency2 = helpers.create_dummy_currency(2)
        self.entity_manager.add_exchange_rate(from_currency = currency1, to_currency = currency2, date = date.today(), rate = 1.2)

        try:
            self.entity_manager.add_exchange_rate(from_currency = currency1, to_currency = currency2, date = date.today(), rate = 1.2)
            self.fail('Added an already existing conversion rate ')
        except(CurrencyException):
            pass
    
    def test_convert_as_list(self):
        """ Retrieve all currencies and convert to format usable in a dropdown as  a tuple of pairs (id, name) """
        for index in range (0, 5):
            helpers.create_dummy_currency(index)
        
        currencies = self.entity_manager.get_currencies_list()
        
        self.assertIsNotNone(currencies)
        self.assertEqual(len(currencies), 5)
        
        for currency in currencies:
            self.assertIsNotNone(currency)
            self.assertEqual(len(currency), 2)
        
        