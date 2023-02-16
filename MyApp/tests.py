from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from .views import index

# Create your tests here.
class IndexViewTestCase(TestCase):
    
    
    def test_index_view_loads(self):
        pass

class IndexViewTestCase(TestCase):
    
    
    def test_index_view_loads(self):
        request = HttpRequest()
        response = index(request)
        self.assertEqual(response.status_code, 200)
        