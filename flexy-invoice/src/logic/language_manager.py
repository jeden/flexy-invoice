'''
Created on Jun 1, 2011

@author: Antonio Bello - Elapsus
'''
from model.domain_models import LanguageEntity
from model.model_utils import DuplicatedEntityException

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
        