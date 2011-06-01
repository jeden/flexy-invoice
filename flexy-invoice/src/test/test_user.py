'''
Created on Apr 28, 2011

@author: Antonio Bello - Elapsus
'''
from test.test_base_appengine_datastore_tester import BaseAppengineDatastoreTester
from logic.user_manager import UserManager
from model.user_models import UserAccountType, UserAccountStatus, UserEntity

from google.appengine.api import users

class Test_User_Manager(BaseAppengineDatastoreTester):
    """ User management tests """
    user_manager = UserManager()
    
    def test_create_user(self):
        """ Test user creation """
        user = self.__create_dummy_user(1)
        
        self.verify_entity_instance(user, UserEntity)
        self.assertEqual(user.account_type, UserAccountType.FREE)
        self.assertEqual(user.account_status, UserAccountStatus.ACTIVE)
        
    def __create_dummy_user(self, index, account_type = UserAccountType.FREE):
        return self.user_manager.register_user(
            google_account = users.User('email_%i@gmail.com' % index),
            account_type = account_type
        )
    
    @classmethod
    def create_dummy_user(cls, index = 1, account_type = UserAccountType.FREE):
        test = Test_User_Manager()
        return test.__create_dummy_user(index, account_type)