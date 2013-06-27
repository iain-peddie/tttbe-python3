#!/usr/bin/env python3

from TestCase import TestCase
from TestResult import TestResult
from WasRun import WasRun


class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())


        
if __name__ == "__main__":
    TestCaseTest("testTemplateMethod").run()
    TestCaseTest("testResult").run()
#    TestCaseTest("testFailedResult").run()
    TestCaseTest("testFailedResultFormatting").run()
