## Variable
### what is Variables

   * Container of date , we need some way of storing any information and manipulate them as well.
### Naming Variable
   * The first character of the identifier must be a letter of the alphabet (uppercase ASCII or lowercase ASCII or Unicode character) 			or an underscore (_).
   * The rest of the identifier name can consist of letters (uppercase ASCII or lowercase ASCII or Unicode character), underscores (_) 			or digits (0-9)
   * Identifier names are case-sensitive. For example, myname and myName are not the same. Note the lowercase n in the former and the 			uppercase N in the latter
## Data Types
   * Variables can hold values of different types called data types.
## Object
   * Python refers to anything used in a program as an object.
## Operators and expressions
   * Operators are the symbols which tells the Python interpreter to do some mathematical or logical operation. 
eg:
```
	>>> 2 + 3
	5
	>>> 23 - 3
	20
	>>> 22.0 / 12
	1.8333333333333333
	>>> 14 % 3(modulue operator)
	2
```
```
=>Relational Operators
< Is less than
<= Is less than or equal to
> Is greater than
>= Is greater than or equal to
== Is equal to
!= Is not equal to
	>>> 1 < 2
	True	
	>>> 3 > 34	
	False
	>>> 23 == 45
	False
	>>> 34 != 323
	True
```
## Logical Operators
   * To do logical AND , OR we use and ,*or* keywords. x and y returns False if x is False else it returns evaluation of y. If x is True, it returns True.
eg:
```
	>>> 1 and 4
	4
	>>> 1 or 4
	1
	>>> -1 or 4
	-1
	>>> 0 or 4
	4
```
=>Shorthand Operator
    * x op= expression is the syntax for shorthand operators. It will be evaluated like x = x op expression
eg:
```
	>>> a = 12
	>>> a += 13 (equal to a = a+1)
	>>> a
	25
```
## Expressions
   * Generally while writing expressions we put spaces before and after every operator so that the code becomes clearer to read, like
eg:
```
	a = 234 * (45 - 56.0 / 34)
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

	 






