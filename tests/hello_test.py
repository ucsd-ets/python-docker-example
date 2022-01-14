import unittest
from app import hello

class TestHello(unittest.TestCase):
    def setUp(self):
        self.hello_world = hello.hello_world
    
    def test_hello(self):
        assert self.hello_world() == 'hello world!'
