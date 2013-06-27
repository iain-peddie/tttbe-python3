#!/usr/bin/env python3

from TestCase import TestCase
from WasRun import WasRun

class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod " == test.log)
        
if __name__ == "__main__":
    TestCaseTest("testTemplateMethod").run()
