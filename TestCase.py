#!/usr/bin/env python3

class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


