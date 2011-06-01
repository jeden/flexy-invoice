'''
Created on Apr 28, 2011

@author: Antonio Bello - Elapsus
'''
from test.test_base_appengine_datastore_tester import BaseAppengineDatastoreTester
from logic.user_manager import UserManager
from model.user_models import UserAccountType, UserAccountStatus, UserEntity
from test import helpers

class Test_User_Manager(BaseAppengineDatastoreTester):
    """ User management tests """
    
    def setUp(self):
        super(Test_User_Manager, self).setUp()
        self._user_manager = UserManager()
    
    def test_create_user(self):
        """ Test user creation """
        user = helpers.create_dummy_user(1, user_manager = self._user_manager)
        
        self.verify_entity_instance(user, UserEntity)
        self.assertEqual(user.account_type, UserAccountType.FREE)
        self.assertEqual(user.account_status, UserAccountStatus.ACTIVE)
