import unittest

from pyapp.hello import hello_world


def test_hello_world():
    assert hello_world() == 'hello world!'
    
class TestHello(unittest.TestCase):
    def setUp(self):
        self.data = [1,2,3,4]
        self.hello_world = hello_world
    
    def test_hello_world(self):
        assert self.hello_world() == 'hello world!'
