from django.test import TestCase

# Create your tests here.
# Test methods have to start with 'test_' 
class BogusTest(TestCase):
    def setUp(self):
        ...
    
    def test_simple_bogus(self):
        self.assertTrue(1 == 1)
    
    