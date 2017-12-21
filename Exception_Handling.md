# Errors and exceptions

Errors or mistakes in a program are often referred to as bugs. They are almost always the fault of the programmer. The process of finding and eliminating errors is called debugging. Errors can be classified into three major groups:

    Syntax errors
    Runtime errors
    Logical errors

Syntax errors

Python will find these kinds of errors when it tries to parse your program, and exit with an error message without running anything.


    leaving out a keyword
    putting a keyword in the wrong place
    leaving out a symbol, such as a colon, comma or brackets
    misspelling a keyword
    incorrect indentation
    empty block


```
myfunction(x, y):
    return x + y

else:
    print("Hello!")

if mark >= 50
    print("You passed!")

if arriving:
    print("Hi!")
esle:
    print("Bye!")

if flag:
print("Flag is set!")


```

Runtime errors

If a program is syntactically correct – that is, free of syntax errors – it will be run by the Python interpreter. 

Some examples of Python runtime errors:

    division by zero
    performing an operation on incompatible types
    using an identifier which has not been defined
    accessing a list element, dictionary value or object attribute which doesn’t exist
    trying to access a file which doesn’t exist


Logical errors

Logical errors are the most difficult to fix. They occur when the program runs without crashing, but produces an incorrect result.


    using the wrong variable name
    indenting a block to the wrong level
    using integer division instead of floating-point division
    getting operator precedence wrong
    making a mistake in a boolean expression
    off-by-one, and other numerical errors


How to handle exceptions?

We use try...except blocks to handle any exception. The basic syntax looks like

```
try:
    statements to be inside try clause
    statement2
    statement3
    ...
except ExceptionName:
    statements to evaluated in case of ExceptionName happens
```


It works in the following way:

        First all lines between try and except statements.
        If ExceptionName happens during execution of the statements then except clause statements execute
        If no exception happens then the statements inside except clause does not execute.
        If the Exception is not handled in the except block then it goes out of try block.



```
>>> def get_number():
...     "Returns a float number"
...     number = float(input("Enter a float number: "))
...     return number
...
>>>
>>> while True:
...     try:
...         print(get_number())
...     except ValueError:
...         print("You entered a wrong value.")
...
Enter a float number: 45.0
45.0
Enter a float number: 24,0
You entered a wrong value.
Enter a float number: Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "<stdin>", line 3, in get_number
KeyboardInterrupt
```

Raising exceptions

One can raise an exception using raise statement.

```
>>> raise ValueError("A value error happened.")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: A value error happened.
```
We can catch these exceptions like any other normal exceptions.
```
>>> try:
...     raise ValueError("A value error happened.")
... except ValueError:
...     print("ValueError in our code.")
...
ValueError in our code.
```
Using finally for cleanup

If we want to have some statements which must be executed under all circumstances, we can use finally clause, it will be always executed before finishing try statements.
```
>>> try:
...     fobj = open("hello.txt", "w")
...     res = 12 / 0
... except ZeroDivisionError:
...     print("We have an error in division")
... finally:
...     fobj.close()
...     print("Closing the file object.")
...
We have an error in division
Closing the file object.
```
In this example we are making sure that the file object we open, must get closed in the finally clause.
