import unittest

import sys

sys.path.append("..")

from pycout import *


class Test(unittest.TestCase):
    def test(self):
        cout << 1000 << "hellos to the world !" << endl;

        self.assertIsInstance(
            cout << "Hello" << " Worlds !" << endl,
            Cout,
            "cout chain must be of type _Cout"
        )


