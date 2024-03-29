'''
Created on Apr 28, 2011

@author: Antonio Bello - Elapsus
'''
from google.appengine.ext import db
from flexy.utils.enum import Enum
from flexy.model.db_model import DbModel

UserAccountType = Enum(['FREE'])
UserAccountStatus = Enum(['ACTIVE'])
    

class UserEntity(DbModel):
    """ User """
    user = db.UserProperty(required = True)
    account_type = db.StringProperty(required = True, choices = UserAccountType)
    account_status = db.StringProperty(required = True, choices = UserAccountStatus, default = UserAccountStatus.ACTIVE)
    
    @classmethod
    def create(cls, user, account_type):
        # check_for_uniqueness(User, 'user', user)
        return cls(user = user, account_type = account_type)