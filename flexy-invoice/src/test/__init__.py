import os

os.environ['AUTH_DOMAIN'] = 'google.com'

from google.appengine.dist import use_library
use_library('django', '1.2')
