# Function
A function is a named sequence of statements
The `def` statement is used to define functions 
It groups a block of code together so that we can call it by name.
It enables us to pass values into the the function when we call it.
It can returns a value (even if None).
When a function is called, it has its own namespace. Variables in the function are local to the function (and disappear when the function exits

## Defining a function

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

### How do you call functions in Python?
Simply write the function's name followed by (), The syntax for calling the new function
```
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
```
Let us write a function which will take two integers as input and then return the sum.

### Example-2

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
### Example-3

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

## Default argument value

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

Remember that you can not have an argument without default argument if you already have one argument with default values before it. Like f(a, b=90, c) is illegal as b is having a default value but after that c is not having any default value.

## Keyword arguments

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
### Example-2
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

## Docstrings

   * In Python we use docstrings to explain how to use the code, it will be useful in interactive mode and to create auto-documentation. 
   * Below we see an example of the docstring for a function called longest_side.

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

## Local Variables

   * When you declare variables inside a function definition, they are not related in any way to other variables with the same names used outside the function - i.e. variable names are local to the function. 
   * This is called the scope of the variable. All variables have the scope of the block they are declared in starting from the point of definition of the name.

```
 x = 50


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)
```

Output:

```
$ python function_local.py
x is 50
Changed local x to 2
x is still 50
```

## The global statement

```
x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)

```
output: 
```
$ python function_global.py
x is 50
Changed global x to 2
Value of x is 2

```


## args and keyword args

  Additional positional arguments passed to a function that are not specified in the function definition (the def: statement``), are collected in an argument preceded by a single asterisk `*args` . 
```
def print_args(*args):
           print(arg) 
```
output:
```
print_args("one", "two", "three")
print_args("one", "two", "three", "four")
```

  Keyword arguments passed to a function that are not specified in the function definition can be collected in a dictionary and passed to an argument preceded by a double asterisk.`**kwargs`
```
def print_kwargs(**kwargs):
       print("%s: %s" % (k, v))

```
output:
```
print_kwargs(name="Jane", surname="Doe")
print_kwargs(age=10)
```

Eg:2

```
def show_args(x, y=-1, *args, **kwargs):
    print '-' * 40
    print 'x:', x
    print 'y:', y
    print 'args:', args
    print 'kwargs:', kwargs

def test():
    show_args(1)
    show_args(x=2, y=3)
    show_args(y=5, x=4)
    show_args(4, 5, 6, 7, 8)
    show_args(11, y=44, a=55, b=66)

test()
```

output:

```
$ python workbook006.py
----------------------------------------
x: 1
y: -1
args: ()
kwargs: {}
----------------------------------------
x: 2
y: 3
args: ()
kwargs: {}
----------------------------------------
x: 4
y: 5
args: ()
kwargs: {}
----------------------------------------
x: 4
y: 5
args: (6, 7, 8)
kwargs: {}
----------------------------------------
x: 11
y: 44
args: ()
kwargs: {'a': 55, 'b': 66}
```
## lambda
  * is anonymous (does not need a name) and
  * contains only an expression and no statements.

```
a = lambda: 3

# is the same as

def a():
    return 3
```

eg-2:

```
>>>fn = lambda x, y, z: (x ** 2) + (y * 2) + z
>>>fn(4, 5, 6)
32

```

## Iterators & Generators


iterator
    And iterator is something that satisfies the iterator protocol. Clue: If it's an iterator, you can use it in a for: statement.
The Iteration Protocol


generator
    A generator is a class or function that implements an iterator, i.e. that implements the iterator protocol.
the iterator protocol

* An object satisfies the iterator protocol if it does the following:

* It implements a `__iter__` method, which returns an iterator object.
* It implements a next function, which returns the next item from the collection, sequence, stream, etc of items to be iterated over
* It raises the StopIteration exception when the items are exhausted and the `next()` method is called.

The built-in function iter takes an iterable object and returns an iterator.
```
>>> x = iter([1, 2, 3])
>>> x
<listiterator object at 0x1004ca850>
>>> x.next()
1
>>> x.next()
2
>>> x.next()
3
>>> x.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

## yield
* The yield statement enables us to write functions that are generators. Such functions may be similar to coroutines, since they may "yield" multiple times and are resumed. 

Generators simplifies creation of iterators. A generator is a function that produces a sequence of results instead of a single value.
```
def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1
```
Each time the yield statement is executed the function generates a new value.
```
>>> y = yrange(3)
>>> y
<generator object yrange at 0x401f30>
>>> y.next()
0
>>> y.next()
1
>>> y.next()
2
>>> y.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
Eg-2:

```
>>> def foo():
...     print "begin"
...     for i in range(3):
...         print "before yield", i
...         yield i
...         print "after yield", i
...     print "end"
...
>>> f = foo()
>>> f.next()
begin
before yield 0
0
>>> f.next()
after yield 0
before yield 1
1
>>> f.next()
after yield 1
before yield 2
2
>>> f.next()
after yield 2
end
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```



