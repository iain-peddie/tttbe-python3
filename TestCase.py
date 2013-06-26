#!/usr/bin/env python3

class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        # default implementation does nothing. This method should
        # be overridden to test anything useful.
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


