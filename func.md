# Function
A function is a named sequence of statements
The `def` statement is used to define functions 
It groups a block of code together so that we can call it by name.
It enables us to pass values into the the function when we call it.
It can returns a value (even if None).
When a function is called, it has its own namespace. Variables in the function are local to the function (and disappear when the function exits

Defining a function

We use def keyword to define a function. General syntax is like
```
def functionname(params):
    statement1
    statement2
```
Example-1

```
def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')
```
How do you call functions in Python?
Simply write the function's name followed by (), The syntax for calling the new function

>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.

Let us write a function which will take two integers as input and then return the sum.

Example-2

```
>>> def sum(a, b):
...     return a + b
```
In the second line with the return keyword, we are sending back the value of a + b to the caller. You must call it like
```
>>> res = sum(3, 5)
>>> res
8
```
Example-3

```
def function_name(arg1, arg2):
    local_var1 = arg1 + 1
    local_var2 = arg2 * 2
    return local_var1 + local_var2
```
here is an example of calling this function:
```
result = function_name(1, 2)
```

Default argument value

In a function variables may have default argument values, that means if we don’t give any value for that particular variable it will be assigned automatically.
```
>>> def test(a , b=-99):
...     if a > b:
...         return True
...     else:
...         return False

```
output:

```
>>> test(12, 23)
False
>>> test(12)
True
```

Important

Important

Remember that you can not have an argument without default argument if you already have one argument with default values before it. Like f(a, b=90, c) is illegal as b is having a default value but after that c is not having any default value.

Keyword arguments

```
>>> def func(a, b=5, c=10):
...     print('a is', a, 'and b is', b, 'and c is', c)
...
>>> func(12, 24)
a is 12 and b is 24 and c is 10
>>> func(12, c = 24)
a is 12 and b is 5 and c is 24
>>> func(b=12, c = 24, a = -1)
a is -1 and b is 12 and c is 24

```
Example-2
```
def sumsub(a, b, c=0, d=0):
    return a - b + c - d
```
output:
```
>>> sumsub(12,4)
8
>>> sumsub(12,4,27,23)
12
>>> sumsub(12,4,d=27,c=23)
4
```

Docstrings

In Python we use docstrings to explain how to use the code, it will be useful in interactive mode and to create auto-documentation. Below we see an example of the docstring for a function called longest_side.

```
import math
def longest_side(a, b):
    """
    Function to find the length of the longest side of a right triangle.

    :arg a: Side a of the triangle
    :arg b: Side b of the triangle

    :return: Length of the longest side c as float
    """
    return math.sqrt(a*a + b*b)
```

(Passing functions as arguments

Higher-order function

Higher-order function or a functor is a function which does at least one of the following step inside:

        Takes one or more functions as argument.
        Returns another function as output.

In Python any function can act as higher order function.

>>> def high(func, value):
...     return func(value)
...
>>> lst = high(dir, int)
>>> print(lst[-3:])
['imag', 'numerator', 'real']
>>> print(lst)

