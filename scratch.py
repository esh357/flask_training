import unittest
from unittest.mock import MagicMock, patch
from urllib import request


class Test:

    def __init__(self):
        self.x = 10

    def do_something(self):
        y = self.do_something_horrible()
        return self.x * 20

    def do_something_horrible(self):
        print(request.getproxies())



class TestTest(unittest.TestCase):

    def setUp(self):
        self.test = Test()

    @patch('scratch.request')
    def test_do_something(self, request):
        request.getproxies = MagicMock(return_value={'x': 'y'})
        #self.test.do_something_horrible = MagicMock(return_value=20)
        self.assertEquals(self.test.do_something(), 200)
        #self.assertEquals(self.test.do_something_horrible.call_count, 1)
