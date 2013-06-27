tttbe-python3
=============

Attempt to work through the python xunit example in Kent Beck's Test-Driven Development ([BECK] )by example, but porting to python3 from python2.

I'll be listing the new types of changes that I have decided to apply by chapter in [BECK] by chapter.

Chapter 18
----------

* Python3's print is a function not an operator. So 
~~~~~ python
print test.wasRun
# becomes
print(test.wasRun)
~~~~~

* classes on the path are injected into a namespace given by their file. So for each class you have, you need a line of the form 

~~~~~ python 
from WasRun import WasRun
 ~~~~~

* Pythonised TestCaseTest to have the usual python pattern for code:
 
~~~~~ python
if __name__ == "__main__":
   TestCaseTest("testRunning").run()
~~~~~

Chapters 19-20
--------------
No further changes needed to be made to make the code in chapter 19 run under python3

Chapter 21
----------
* TestResult needs to be imported to the classes using it properly

* Converted formatting to python3 formatting, which doesn't require formatting types by
default. For example, the first update of TestResult to return a runCount read from the object
was

~~~~~ python
return "%d run, 0 failed" % self.runCount
~~~~~

This becomes:

~~~~~ python
return "{} run, 0 failed".format(self.runCount)
~~~~~

Chapter 22
----------
No new changes were needed.
   
Copying
=======

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
