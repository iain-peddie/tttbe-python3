#!/usr/bin/env python3

from TestCase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.name = name
        
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "

