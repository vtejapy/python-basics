# Modules
Modules are reusable libraries of code in Python. Python comes with many standard library modules.

A module is imported using the import statement.

```
>>> import time
>>> print time.asctime()
'Fri Mar 30 12:59:21 2012'
```

In this example, we’ve imported the time module and called the asctime function from that module, which returns current time as a string.

There is also another way to use the import statement.
```
>>> from time import asctime
>>> asctime()
'Fri Mar 30 13:01:37 2012'
```
Here were imported just the asctime function from the time module.


Writing our own modules is very simple.

For example, create a file called num.py with the following content.
```
def square(x):
    return x * x

def cube(x):
    return x * x * x
```

```

>>> import num
>>> num.square(3)
9
>>> num.cube(3)
27
```

```
"""
Bars Module
============
This is an example module with provide different ways to print bars.
"""

def starbar(num):
    """Prints a bar with *

    :arg num: Length of the bar
    """
    print('*' * num)

def hashbar(num):
    """Prints a bar with #

    :arg num: Length of the bar
    """
    print('#' * num)

def simplebar(num):
    """Prints a bar with -

    :arg num: Length of the bar
    """
    print('-' * num)



>>> import bars
>>>
>>> bars.hashbar(10)
##########
>>> bars.simplebar(10)
----------
>>> bars.starbar(10)
**********
```





