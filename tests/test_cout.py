import unittest

from pycout import *
from pycout.cout import Cout


class Test(unittest.TestCase):

    def test(self):
        # cast providing non-str does not break
        cout << 1000 << " hellos to the world!" << endl

        partial_cout = cout << "Hello" << " World!"

        self.assertEqual(partial_cout << 0, Cout("Hello World!0"))
        self.assertEqual(partial_cout << 1, Cout("Hello World!1"))

        self.assertIsNone(partial_cout << endl)
        self.assertEqual(partial_cout << 1, Cout("Hello World!1"))

        self.assertIsNone(partial_cout << endl)
