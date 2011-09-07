'''
Created on Sep 6, 2011

@author: Antonio Bello - Elapsus
'''
from logic.user_manager import UserManager
from flexy.web.control.user_session import UserSessionBase

class UserSession(UserSessionBase):
    def _on_load_user(self, account):
        return UserManager.retrieve_user_by_account(account)