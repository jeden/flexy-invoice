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
from view.client_view import AddClientHandler, ListClientsHandler, ListClientsAsync
from view.invoice_view import CreateInvoiceHandler
from flexy.utils.rendering import render_template

class MainHandler(webapp.RequestHandler):
    def get(self):
        if not render_template(self, self.request.path):
            render_template(self)

def main():
    application = webapp.WSGIApplication([
                                        ('/p/client/list', ListClientsHandler),
                                         ('/p/client/add', AddClientHandler),
                                         ('/p/invoice/create', CreateInvoiceHandler),
                                         ('p/async/client/list', ListClientsAsync)],
                                         debug = True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
