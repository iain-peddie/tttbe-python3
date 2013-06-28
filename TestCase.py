#!/usr/bin/env python3

from TestResult import TestResult
import traceback

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

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception as ex:
            traceback.print_exc()
#            print(ex)
#            print(ex.stackTrace())
            result.testFailed()
        self.tearDown()


