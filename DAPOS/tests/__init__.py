import os
import unittest


def suite():
    suite = unittest.TestLoader()
    tests = suite.discover(os.path.dirname(__file__))
    return tests
