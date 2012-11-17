"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client
from rest_framework import status
from rest_framework.parsers import JSONParser

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
             
"""
class FamilyApiTest(TestCase):
    def test_create_delete_family(self):
        c = Client()
        response = c.post('/families', '{"name": "testFamily123"}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        data = JSONParser().parse(response)      
        self.assertEqual(data['name'], 'testFamily123')
        pk = data['pk'] 
        response = c.delete('/families/' + pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
"""        