#!/usr/bin/env python3

from TestCase import TestCase
from WasRun import WasRun

class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)
        
if __name__ == "__main__":
    TestCaseTest("testRunning").run()
