#!/usr/bin/env python3

from TestCase import TestCase
from TestResult import TestResult
from WasRun import WasRun
from TestSuite import TestSuite


class TestCaseTest(TestCase):

    def setUp(self):
        self.result = TestResult();

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())
        
if __name__ == "__main__":
    testMethods = [ "testTemplateMethod",
                    "testResult", 
                    "testFailedResultFormatting",
                    "testFailedResult", 
                    "testSuite"
                    ];
    suite = TestSuite()
    for method in testMethods:
        case = TestCaseTest(method)
        suite.add(case)
    
    result = TestResult()
    suite.run(result)

    print("{} : {}".format(method, result.summary()))
