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
from util import render_template
from view.signup_view import SignupHandler

class MainHandler(webapp.RequestHandler):
    def get(self):
        if not render_template(self, self.request.path):
            render_template(self)

def main():
    application = webapp.WSGIApplication([
                                          ('/signup', SignupHandler),
                                          ('/.*', MainHandler)],
                                         debug = True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
