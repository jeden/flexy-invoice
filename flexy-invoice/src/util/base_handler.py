'''
Created on May 24, 2011

@author: Antonio Bello - Elapsus
'''
from google.appengine.ext import webapp
import logging
from google.appengine.api import users
from util.user_session import UserSession

class BaseHandler(webapp.RequestHandler):
    """
    Base handler to handle application wide exceptions
    """
    def initialize(self, request, response):
        """ Override to inizialize the session """
        super(BaseHandler, self).initialize(request, response)
        self._user_session = UserSession(users.get_current_user())
    
    def handle_exception(self, exception, debug_mode):
        if debug_mode:
            webapp.RequestHandler.handle_exception(self, exception, debug_mode)
        else:
            logging.exception(exception)
            self.error(500)
            
            # TODO: Redirect to proper page
            
class BaseProtectedHandler(BaseHandler):
    """
    Request handler for protected pages
    """
    def initialize(self, request, response):
        super(BaseProtectedHandler, self).initialize(request, response)
        if self._user_session.is_registered() == False:
            self.redirect('/signup')
                