#!/usr/bin/env python3

from TestResult import TestResult

class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        """default implementation does nothing. 

        This method is called before each test is run. Test classes which need
        setup code should override this method."""

    def tearDown(self):
        """Default implementation does nothing.

        This method is called after each test has run. Test classes which need
        teardown code should override this method."""

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return TestResult()


