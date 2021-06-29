from django.test import TestCase

# Create your tests here.
from django.test import RequestFactory, TestCase


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_ackermann(self):
        print('\n\tackermann test cases:')
        print('\t\ttest ackermann should return 200 with correct value')
        request = self.factory.get('discount-code/')

