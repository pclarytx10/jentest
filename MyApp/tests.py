if __name__ == '__MyApp__':
    unittest.MyApp()

from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from .views import home, about

# Create your tests here.


class HomeViewTestCase(TestCase):

    def test_home_view_loads(self):
        pass


class HomeViewTestCase(TestCase):

    def test_home_view_loads(self):
        request = HttpRequest()
        response = home(request)
        self.assertEqual(response.status_code, 200)


class AboutViewTestCase(TestCase):

    def test_about_view_loads(self):
        pass


class AboutViewTestCase(TestCase):

    def test_about_view_loads(self):
        request = HttpRequest()
        response = about(request)
        self.assertEqual(response.status_code, 200)
