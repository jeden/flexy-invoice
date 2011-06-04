'''
Created on May 23, 2011

@author: Antonio Bello - Elapsus
'''

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
from view.client_view import AddClientHandler
from util import render_template
from view.invoice_view import CreateInvoiceHandler

class MainHandler(webapp.RequestHandler):
    def get(self):
        if not render_template(self, self.request.path):
            render_template(self)

def main():
    application = webapp.WSGIApplication([
                                         ('/p/client/add', AddClientHandler),
                                         ('/p/invoice/create', CreateInvoiceHandler)],
                                         debug = True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
