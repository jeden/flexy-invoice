'''
Created on Jun 1, 2011

@author: Antonio Bello - Elapsus
'''
from model.domain_models import LanguageEntity
from flexy.model.db_model import DuplicatedEntityException

class LanguageException(Exception):
    pass

class LanguageManager:
    @classmethod
    def create_language(self, name):
        try:
            language = LanguageEntity.create(name = name)
            language.put()
        except DuplicatedEntityException:
            raise LanguageException
        
        return language
    
    @classmethod
    def list_languages(cls):
        """
            Return the list of languages as a list of pairs:
            ((1, "Italian"), ...)
        """
        languages = LanguageEntity.all().order('name').run()
        list = [(language.key().id(), language.name) for language in languages]
        
        return list
        
    @classmethod
    def listify_languages(cls):
        '''
            Return the list of languages, formatted to be used in a listbox 
            as a list of tuples (id, name)
            An element representing no selection is added at top
        '''
        list = cls.list_languages()
        list.insert(0, ('', ''))
        return list
        
    @classmethod
    def find_by_id(cls, language_id):
        return LanguageEntity.get_by_id(language_id) 
        