#!/usr/bin/env python3

class TestResult:

    def __init__(self):
        self.runCount = 0

    def testStarted(self):
        self.runCount += 1
    
    def summary(self):
        return "{} run, 0 failed".format(self.runCount)
