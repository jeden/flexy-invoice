# ------------
# Ensure this block is at beginning of file

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.dist import use_library
use_library('django', '1.2')

# End block
# ------------

import wsgiref
from google.appengine.ext import webapp
from view.signup_view import SignupHandler
from flexy.utils.rendering import render_template

class MainHandler(webapp.RequestHandler):
    def get(self):
        if not render_template(self, 'home.html', {}):
            render_template(self)

def main():
    application = webapp.WSGIApplication([
                                          ('/signup', SignupHandler),
                                          ('/.*', MainHandler)],
                                         debug = True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
