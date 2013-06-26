#!/usr/bin/env python3

from TestCase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        self.wasSetUp = None
        TestCase.__init__(self, name)
        self.name = name
        
    def setUp(self):
        self.wasSetUp = 1

    def testMethod(self):
        self.wasRun = 1

