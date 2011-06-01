'''
Created on May 26, 2011

@author: Antonio Bello - Elapsus
'''
from google.appengine.api import memcache, users
from logic.user_manager import UserManager, UserNotFoundException

class UserSession:
    def __init__(self, account):
        self._verify_user(account)
        
    def is_logged_in(self):
        """
        Return true if the user is authenticated 
        """
        return self._is_logged_in
    
    def is_registered(self):
        """
        Return true if the user is registered and authenticated 
        """
        return self._is_registered
    
    def get_account(self):
        return self._account
    
    def get_user(self):
        return self._user
    
    def refresh(self):
        """ Refresh the user status """
        memcache.delete(self._account.user_id())
        self._verify_user(self._account)
        
        
    def _verify_user(self, account):
        self._account = account
        self._user = memcache.get(self._account.user_id())
        
        if self._user is None:
            try:
                self._user = UserManager.retrieve_user_by_account(account)
                memcache.add(self._account.user_id(), self._user)
            except UserNotFoundException:
                self._user = None
                
        self._is_logged_in = self._account is not None
        self._is_registered = self._user is not None
        