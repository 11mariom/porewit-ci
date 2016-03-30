from unittest import TestCase

class TestHello(TestCase):

    def test_hello(self):
        s = "Hello World"

        self.assertEqual(s, "Hello World")
