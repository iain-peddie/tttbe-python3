#!/usr/bin/env python3

from TestCase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)
        self.name = name

    def testMethod(self):
        self.wasRun = 1

