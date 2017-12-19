# what is python ?
  * Python is a high-level general purpose programming language:
    * Because code is automatically compiled to byte code and executed, Python is suitable for use as a scripting language, Web application implementation language, etc.
    * Because Python can be extended in C and C++, Python can provide the speed needed for even compute intensive tasks.
    * Because of its strong structuring constructs (nested code blocks, functions, classes, modules, and packages) and its consistent use of objects and object-oriented programming, Python enables us to write clear, logical applications for small and large tasks.
  * Important features of Python:
    * Built-in high level data types: strings, lists, dictionaries, etc.
    * The usual control structures: if, if-else, if-elif-else, while, plus a powerful collection iterator (for).
    * Multiple levels of organizational structure: functions, classes, modules, and packages. These assist in organizing code. An excellent and large example is the Python standard library.
    * Compile on the fly to byte code -- Source code is compiled to byte code without a separate compile step. Source code modules can also be "pre-compiled" to byte code files.
    * Object-oriented -- Python provides a consistent way to use objects: everything is an object. And, in Python it is easy to implement new object types (called classes in object-oriented programming).
  * Some things you will need to know:

    Python uses indentation to show block structure. Indent one level to show the beginning of a block. Out-dent one level to show the end of a block. As an example, the following C-style code:
```
    if (x)
    {
        if (y)
        {
            f1()
        }
        f2()
    }
```
in Python would be:
```
    if x:
        if y:
            f1()
        f2()
```
And, the convention is to use four spaces (and no hard tabs) for each level of indentation. Actually, it's more than a convention; it's practically a requirement. Following that "convention" will make it so much easier to merge your Python code with code from other sources.

## An overview of Python:

   * A scripting language -- Python is suitable (1) for embedding, (2) for writing small unstructured scripts, (3) for "quick and dirty" programs.

   * Not a scripting language -- (1) Python scales. (2) Python encourages us to write code that is clear and well-structured.

   * Interpreted, but also compiled to byte-code. Modules are automatically compiled (to .pyc) when imported, but may also be explicitly compiled.

   * Provides an interactive command line and interpreter shell. In fact, there are several.

   * Dynamic -- For example:
        * Types are bound to values, not to variables.
        * Function and method lookup is done at runtime.
        * Values are inspect-able.
        * There is an interactive interpreter, more than one, in fact.
        * You can list the methods supported by any given object.

   * Strongly typed at run-time, not compile-time. Objects (values) have a type, but variables do not.

   * Reasonably high level -- High level built-in data types; high level control structures (for walking lists and iterators, for example).

   * Object-oriented -- Almost everything is an object. Simple object definition. Data hiding by agreement. Multiple inheritance. Interfaces by convention. Polymorphism.

   * Highly structured -- Statements, functions, classes, modules, and packages enable us to write large, well-structured applications. Why structure? Readability, locate-ability, modifiability.
  
   * Indented block structure -- "Python is pseudo-code that runs."

   * Automatic garbage collection. (But, there is a gc module to allow explicit control of garbage collection.)
 ## Python interpreter
 ### There are two modes for using the Python interpreter:
     * Interactive Mode
     * Script Mode

## Comments
Comments are any text to the right of the # symbol and is mainly useful as notes for the reader of the program.
eg:
```
	print('hello world') # Note that print is a function

			or
	# Note that print is a function
	print('hello world')
```
### Use as many useful comments as you can in your program to:
     * explain assumptions
     * explain important decisions
     * explain important details
     * explain problems you're trying to solve
     * explain problems you're trying to overcome in your program, etc 
### types of comments
	* single line comment use (#)
        * Multiple line comments use(''' or """)

## Indentation
   * Whitespace is important in Python. Actually, whitespace at the beginning of the line is important. This is called indentation. 
   * Leading whitespace (spaces and tabs) at the beginning of the logical line is used to determine the indentation level of the logical line, which in turn is used to determine the grouping of statements.
   * This means that statements which go together must have the same indentation.Each such set of statements is called a block
eg:
```
		i = 5
		# Error below! Notice a single space at the start of the line
		 print('Value is', i)
		print('I repeat, the value is', i)

	output:

```		  File "whitespace.py", line 3
		    print('Value is', i)
 		    ^
	          IndentationError: unexpected indent
```
## How to indent ?
   * Use four spaces for indentation. This is the official Python language recommendation. Good editors will automatically do this for you.like pycharm,atom,sublime,eclipse..etc
		


## Literal Constants
   * An example of a literal constant is a number like 5, 1.23, or a string like 'This is a string' or "It's a string!"
##  Numbers
    * Numbers are mainly of two types - integers and floats.
    * There is no separate long type. The int type can be an integer of any size.

eg:
	An example of an integer is 2 which is just a whole number.

## Strings
   * A string is a sequence of characters. Strings are basically just a bunch of words.
   * You will be using strings in almost every Python program that you write, so pay attention to the following part.
   *Single Quote
       * You can specify strings using single quotes such as 'Quote me on this'
       * All white space i.e. spaces and tabs, within the quotes, are preserved as-is
   * Double Quotes
       * Strings in double quotes work exactly the same way as strings in single quotes. An example is "What's your name?"
   * Triple Quotes {#triple-quotes}
       * You can specify multi-line strings using triple quotes(""" or ''')You can use single quotes and double quotes freely within the 	triple quotes.
       eg:
```
	'''This is a multi-line string. This is the first line.
	This is the second line.
	"What's your name?," I asked.
	He said "Bond, James Bond."
	'''
```
   * Strings Are Immutable
      * This means that once you have created a string, you cannot change it.
## format method
   * Sometimes we may want to construct strings from other information. This is where the format() method is useful.
   * A string can use certain specifications and subsequently, the format method can be called to substitute those specifications with corresponding arguments to the format method.
eg:
```
	age = 20
	name = 'Danny'
	print('{0} was {1} years old when he wrote this book'.format(name, age))
	print('Why is {0} playing with that python?'.format(name))
```
output:
```
	$ python str_format.py
	Danny was 20 years old when he wrote this book
	Why is Danny playing with that python?
```
eg2:
	age = 20
	name = 'Danny'

	print('{} was {} years old when he wrote this book'.format(name, age))
	print('Why is {} playing with that python?'.format(name))

## Escape Sequences
    * Suppose, you want to have a string which contains a single quote ('), how will you specify this string? For example, the string is "What's your name?". You cannot specify 'What's your name?' because Python will be confused as to where the string starts and ends. So, you will have to specify that this single quote does not indicate the end of the string. This can be done with the help of what is called an escape sequence.
	* you can specify the string as 'What\'s your name?' or "What's your name?"
        * the newline character - \n
		eg:
```
			'This is the first line\nThis is the second line'
```
        	output:
```
			"This is the first line. 
			This is the second line"
```
        =>the tab: \t

		eg:
```
			'This is the first line\t\t\t\t\tThis is the second line'
```
		output:
```
			"This is the first line      This is the second line"
```
## Variable
   * Container of date , we need some way of storing any information and manipulate them as well.
	* Naming
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
=>Relational Operators
< Is less than
<= Is less than or equal to
> Is greater than
>= Is greater than or equal to
== Is equal to
!= Is not equal to
eg:
```
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

	 







