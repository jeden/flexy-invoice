import os
import unittest
from google.appengine.api import apiproxy_stub_map, datastore_file_stub
from google.appengine.ext import db

os.environ['APPLICATION_ID'] = 'FlexyPlex'

class BaseAppengineDatastoreTester(unittest.TestCase):

    def setUp(self):
        # Required to use the datastore in a testing environment
        app_id = 'myapp'
        os.environ['APPLICATION_ID'] = app_id
        datastore_file = '/dev/null'
        apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap()
        stub = datastore_file_stub.DatastoreFileStub(app_id, datastore_file, '/')
        apiproxy_stub_map.apiproxy.RegisterStub('datastore_v3', stub)

    def __init__(self, methodName = None):
        """ 
        Constructor override to allow creation of an instance
        to be used outside the test run process
        Useful for defining helper methods reusable in 
        other test classes
        """
        
        if methodName != None:
            unittest.TestCase.__init__(self, methodName)
        else:
            # Map types to custom assertEqual functions that will compare
            # instances of said type in more detail to generate a more useful
            # error message.
            # Copied from unittest.TestCase
            self._type_equality_funcs = {}
            self.addTypeEqualityFunc(dict, self.assertDictEqual)
            self.addTypeEqualityFunc(list, self.assertListEqual)
            self.addTypeEqualityFunc(tuple, self.assertTupleEqual)
            self.addTypeEqualityFunc(set, self.assertSetEqual)
            self.addTypeEqualityFunc(frozenset, self.assertSetEqual)
            self.addTypeEqualityFunc(unicode, self.assertMultiLineEqual)
            
    def verify_entity_instance(self, instance = None, type = None):
        """ verify that instance is not null, of the specified type, and having a not null key """
        self.assertIsNotNone(instance)
        self.assertIsInstance(instance, type)
        self.assertIsInstance(instance.key(), db.Key)
            