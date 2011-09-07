'''
Created on May 21, 2011

@author: Antonio Bello - Elapsus
'''

# Required to make django work
# Do not remove

from util.session import UserSession
from flexy.web.handler.base_handler import BaseHandler

BaseHandler._UserSessionClass = UserSession