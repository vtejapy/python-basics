## Variable
### what is Variables

   * Container of date , we need some way of storing any information and manipulate them as well.
### Naming Variable
   * The first character of the identifier must be a letter of the alphabet (uppercase ASCII or lowercase ASCII or Unicode character) 			or an underscore (_).
   * The rest of the identifier name can consist of letters (uppercase ASCII or lowercase ASCII or Unicode character), underscores (_) 			or digits (0-9)
   * Identifier names are case-sensitive. For example, myname and myName are not the same. Note the lowercase n in the former and the 			uppercase N in the latter
## Data Types in Python
  * Everything in Python programming is an object, and each object has its own unique identity(a type and a value).

  * There are many native(built-in) data types available in Python.

## Some important are:

   * Numbers: An are integers (such as 1, 2, 3…), floats (such as 2.6, 4.8 etc), fractions (such as ½. ¾ etc) or even complex numbers.
        - int (signed integer)
        - float
        - long
        - complex
   * Sequences:
        - Strings: Sequence of Unicode characters, like an HTML document.
        - Bytes/Byte array: Any type of file.
        - Lists: An ordered sequence of values.
        - Tuples: An ordered immutable sequence of values.

   * Boolean: Holds either true or false values.
   * Sets: An unordered container of values.
   * Dictionaries: An key-paired values set in an unordered way.
### Keywords 
The following identifiers are used as reserved words, or keywords of the language, and cannot be used as ordinary identifiers. They must be typed exactly as written here:
```
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
```

## Object
   * Python refers to anything used in a program as an object.
## Multiple Assignment
With Python, you can assign one single value to several variables at the same time. This lets you initialize several variables at once, which you can reassign later in the program yourself, or through user input.

Through multiple assignment, you can set the variables x, y, and z to the value of the integer 0:
```
x = y = z = 0
print(x)
print(y)
print(z)
```
Output
```
0
0
0
```
## Conversions
    * Convert from one type to another type
eg:
```
	>>> a = 5
	>>> type(a)
	<type 'int'>
	>>> a = str(a)
	>>> a
	'5'
	>>> type(a)
	<type 'str'>
```

	 






