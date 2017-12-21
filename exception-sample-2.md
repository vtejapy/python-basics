You can raise an exception with the try/except statements, which full syntax is:

>>> try:
>>>     open("tmp/non-existing-file.tttt")
>>> except IOError:
>>>     print "The file '/tmp/non-existing-file.ttt' does not exist"
>>> finally:
>>>     print 'Whatever the results is we can enter here, to properly close the file for instanece.'
>>> else:
>>>     print "Well, the file exists despite itscrazy name: the else clause is executed."

Note that in general most code includes only the try/except:

>>> try:
>>>     open("tmp/non-existing-file.tttt")
>>> except IOError:
>>>     print "The file 'tmp/non-existing-file.ttt' does not exist"

or directly with the raise keyword:

x = 0.
if x == 0:
    raise ZeroDivisionError
else:
    return 1./x

3.2. Explanation

The try/except example is quite straightforward to understand given the print statements. The only tricky part is the IOError. This is an exception, that is a predefined error in Python language. There are a bunch of them like TypeError, ZeroDivisionError and so on (see below for more details).

The idea is that if you know that a specific error might occur, then you should use the try/except to catch this particular error.

The more general usage of the except block is to provide an exception and its argument:

try:
     1/0
except Exception, e:
    print(e)

In fact e is the exception argument that you can introspect:

e.args
e.message

3.3. Multiple exceptions

You can put multiple exeception in the except statement as follows:

>>> try:
>>>     x = input('Enter the first number: ')
>>>     y = input('Enter the second number: ')
>>>     print x/y
>>> except (ZeroDivisionError, TypeError), e:
>>>     print 'Your numbers were bogus...'
>>>     print e

you may decide not to set any exception:

>>> try:
>>>    try_statements
>>> except:
>>>    except_statements

This try-except statement catches all the exceptions that occur. However, it is not considered a good programming practice, because it does not make the programmer identify the root cause of the problem that may occur.
3.4. Ignoring an exception

You can ignore an exception by catching it:

x = -10
try:
    import math
    print math.sqrt(x)
except ValueError, e:
    import cmath
    print cmath.sqrt(x)

Of course this example is simple, you can have test if the number is negative before hand but it shows how to catch an error and fix the problem within your code. You could also simply do nothing if the number if negative:

x = -10
try:
    import math
    print math.sqrt(x)
except:
    pass

3.5. What are the existing exceptions ?

>>> import exceptions
>>> dir(exceptions)
['ArithmeticError', 'AssertionError', 'AttributeError', ...]

3.6. User-defined exceptions

Although there are quite a lot of exceptions, you can also define your own exception. The following example (From Python website exceptions) illustrates the syntax and usage:

>>> class MyError(Exception):
...     def __init__(self, value):
...         self.value = value
...     def __str__(self):
...         return repr(self.value)
...
>>> try:
...     raise(MyError(2*2))
... except MyError, e:
...     print 'My exception occured, value:', e.value
My exception occured, value: 4

3.7. Cleanup using the finally or with statement

The finally block is run whatever is the outcome of the try block. This is particurlaly useful in the context of file manipulation.:

try:
    f = open("temp.txt", "w")
    # something wrong here e.g. cannot open the file
except IOError, e:
    print e
finally:
    f.close()

Another way to ensure the previous cleanup action is to use the with statement. Let consider this code that prints a file contents with numbers for each line (withouth the with statement):

num = 1
f = open(fname)
for line in f:
    print("%d %s" % (num, line))
    num += 1

if you don’t call the close statement specifically, we don’t know precisey when the file will be closed. Instead, the same code can be written with the with statement as follows:

num = 1
with open(fname, "r") as f:
    for line in f:
        print("%d %s" % (num, line))
        num += 1

With the with statement; the file is closed immediately after the for loop.
3.8. Exception hierarchy

From Python website (exception-hierarchy):

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
      |    +-- BufferError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
       +-- ImportWarning
       +-- UnicodeWarning
       +-- BytesWarning

3.9. A note about assertion

You can perform quick sanity check using assertion and the assert() function:

assert x > 0, "x must be greater than zero"

Nevertheless, asserts usage are not recommended because they are disabled if Python is started with the optimisation option -O. It should be used for debugging only. Note that you can use built-in value __debug__ to include debugging code.
