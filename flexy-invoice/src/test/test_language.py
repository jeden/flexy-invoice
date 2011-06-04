'''
Created on Jun 1, 2011

@author: Antonio Bello - Elapsus
'''
from test.test_base_appengine_datastore_tester import BaseAppengineDatastoreTester
from test import helpers
from model.domain_models import LanguageEntity
from logic.language_manager import LanguageException, LanguageManager

class Test_Language(BaseAppengineDatastoreTester):
    """ Language related tests """
    
    def setUp(self):
        super(Test_Language, self).setUp()
        
    def test_create_language(self):
        """ Test new language creation """
        language = helpers.create_dummy_language(1)
        self.verify_entity_instance(language, LanguageEntity)
    
    def test_create_existing_language(self):
        """ Verify that adding an existing language generates an exception """
        helpers.create_dummy_language(1)
        try:
            helpers.create_dummy_language(1)
            self.fail('Created duplicated language')
        except (LanguageException):
            pass
            
    def test_convert_as_list(self):
        """ Retrieve all languages and convert to format usable in a dropdown as  a tuple of pairs (id, name) """
        for index in range (0, 5):
            helpers.create_dummy_language(index)
        
        languages = LanguageManager.list_languages()
        
        self.assertIsNotNone(languages)
        self.assertEqual(len(languages), 5)
        
        for language in languages:
            self.assertIsNotNone(language)
            self.assertEqual(len(language), 2)