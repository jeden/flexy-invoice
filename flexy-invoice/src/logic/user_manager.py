'''
Created on Apr 28, 2011

@author: Antonio Bello - Elapsus
'''
from model.user_models import UserEntity

class UserManager:
    """ User management """
    
    def register_user(self, user, account_type):
        """ Register a new user """
        user = UserEntity.create(user = user, account_type = account_type)
        user.put()
        
        return user