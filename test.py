import os
from login import App
import unittest
import tempfile

def hold_response(test):
   def keep_last_response(self):
      global response
      response = test(self)
      return response
   return keep_last_response  
      
class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, App.config['DATABASE'] = tempfile.mkstemp()
        App.config['TESTING'] = True
        self.app = App.test_client()
        
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(App.config['DATABASE'])
   
    def test_home(self):
        self.assertIn('Home page',self.app.get('/').data)  
        return  self.app.get('/')

    def test_login_302_status(self):
        self.assertEqual('302 FOUND', self.app.get('/members').status)

     
if __name__ == '__main__':
    unittest.main()
