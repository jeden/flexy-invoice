'''
Created on May 24, 2011

@author: Antonio Bello - Elapsus
'''
from google.appengine.api import users
from logic.user_manager import UserManager
from util import render_template
from model.user_models import UserAccountType
from util.base_handler import BaseHandler

class SignupHandler(BaseHandler):
    def get(self):
        login_url = (self._user_session.is_logged_in() == False) and users.create_login_url(dest_url = 'http://localhost:8080/signup') or None
    
        if self._user_session.is_logged_in() and self._user_session.is_registered():
            self.redirect('/')
        else:        
            return render_template(self, 'signup.html', {
                                                            'is_logged_in': self._user_session.is_logged_in(),
                                                            'is_registered': self._user_session.is_registered(),
                                                            'login_url': login_url
                                                         })
    def post(self):
        if not self._user_session.is_logged_in():
            # User not signed in yet
            self.redirect('/signup')
        else:
            if not self._user_session.is_registered():
                # User signed in, but not registered yet
                user = UserManager.register_user(self._user_session.get_account(), UserAccountType.FREE)
            
            # Register the user id into the session
            self._user_session.refresh()
            
            self.redirect('/')
