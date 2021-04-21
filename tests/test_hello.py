import unittest

from pyapp import hello_world


def test_hello_world():
    assert hello_world() == 'hello world!'
    
class TestHello(unittest.TestCase):
    def setUp(self):
        self.hello_world = hello_world
    
    def test_hello_world(self):
        assert self.hello_world() == 'hello world!'
