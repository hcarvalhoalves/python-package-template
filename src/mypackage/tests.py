import unittest

class MyTest(unittest.TestCase):
    def test_foo(self):
        self.assertTrue('foo' is 'foo')
