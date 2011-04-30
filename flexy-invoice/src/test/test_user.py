'''
Created on Apr 28, 2011

@author: Antonio Bello - Elapsus
'''
from test.test_base_appengine_datastore_tester import BaseAppengineDatastoreTester
from logic.user_manager import UserManager
from model.user_models import UserEntity, UserAccountType, UserAccountStatus

from google.appengine.api.users import User

class Test_User_Manager(BaseAppengineDatastoreTester):
    """ User management tests """
    user_manager = UserManager()
    
    def test_create_user(self):
        user = self.__create_dummy_user(1)
        self.verify_entity_instance(user, UserEntity)
        self.assertEqual(user.account_type, UserAccountType.FREE)
        self.assertEqual(user.account_status, UserAccountStatus.ACTIVE)
        
    def __create_dummy_user(self, index, account_type = UserAccountType.FREE):
        return self.user_manager.register_user(
            user = User(email = 'email_%i@gmail.com' % index, _auth_domain = 'gmail.com'),
            account_type = account_type
        )
        