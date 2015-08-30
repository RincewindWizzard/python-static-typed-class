#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import unittest
from static_typed import *

class Person(Model):    # subclass Model to get Constructor and __repr__
    name    = Type(str)
    age     = Type(int, 0) # default 0
    married = Type(bool, False)
    __cons__= ['name', 'age', 'married']   # specify this to use constructor without named arguments


class TestDescriptors(unittest.TestCase):
    def test_person(self):
        mary = Person("Mary", 25, married=True)
        self.assertEqual(mary.age, 25)
        mary.age = "26"
        self.assertEqual(mary.age, 26)
        self.assertEqual(mary.name, "Mary")
        self.assertTrue(mary.married)


if __name__ == '__main__':
    unittest.main()
