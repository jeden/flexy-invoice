'''
Created on Apr 28, 2011

@author: Antonio Bello - Elapsus
'''
from model.user_models import UserEntity

class UserNotFoundException(Exception):
    pass

class UserManager:
    """ User management """
    
    @classmethod
    def register_user(cls, google_account, account_type):
        """ 
            Register a new user account 
            
            Return the user entity
        """
        user = UserEntity.create(user = google_account, account_type = account_type)
        user_key = user.put()
        return cls.retrieve_user_by_key(user_key)
    
    @classmethod
    def retrieve_user_by_account(cls, google_account):
        """ 
            Retrieve the entity user associated to a google account 
            Throw a UserNotFoundException if no user is found
        """
        user = UserEntity.gql('WHERE user = :1', google_account).get()
        if user is None:
            raise UserNotFoundException
        
        return user
    
    @classmethod
    def retrieve_user_by_key(cls, user_key):
        """ 
            Retrieve a user by key
            Throw a UserNotFoundException if no user is found
        """
        user = UserEntity.get(user_key)
        if user is None:
            raise UserNotFoundException
        
        return user