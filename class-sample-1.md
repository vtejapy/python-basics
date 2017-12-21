Defining Class And Object

A class is a technique to group functions and data members and put them in a container so that they can be accessed later by using dot (.) operator. Objects are the basic runtime entities of object-oriented programming. It defines the instance of a class. Objects get their variables and functions from classes and the class we will be creating are the templates made to create the object.
Object-Oriented Terminologies

    class: Classes are a user-defined data type that is used to encapsulate data and associated functions together. It also helps in binding data together into a single unit.
    Data Member: A variable or memory location name that holds value to does a specific task within a program.
    Member Function: They are the functions; usually a block of a code snippet that is written to re-use it.
    Instance variable: A variable that is defined inside a method of a class.
    Function Overloading: This technique is used to assign multiple tasks to a single function & the tasks are performed based on the number of argument or the type of argument the function has.
    Operator Overloading: It is the technique of assigning multiple function/tasks to a particular operator.
    Inheritance: It is the process of acquiring the properties of one class to another i.e. one class can acquire the properties of another.
    Instantiation: It is the technique of creating an instance of a class.

Program For Class In Python
Example:

#!/usr/bin/python

class karl :
	varabl = 'Hello'

def function(self) :
	print "This is a message Hello"

Another program to explain functions inside a class:
Example:

#!/usr/bin/python

class karl(object) :
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def sample(self) :
		print " This is just a sample code"

In the above code, we created a class name karl using ‘class’ keyword. And two functions are used namely __init__() (for setting the instance variable) & sample(). Classes are used instead of modules because programmers can take this class ‘karl’ & use it or modify it as many times as we want & each one won’t interfere with each other. Importing a module brings the entire program into use.
Creating Objects (Instance Of A Class)

Let’s see an example to show how to create an object:
Example:

#!/usr/bin/pythonclass student:
class student:
        def __init__(self, roll, name):
                self.r = roll
                self.n = name
                print ((self.n))
                
#...       
stud1 = student(1, "Alex")
stud2 = student(2, "Karlos")

print (("Data successfully stored in variables"))

Output:

Alex
Karlos
Data successfully stored in variables

Accessing Object Variables

We can access the object’s variable using dot (.) operator.
The syntax is:

my object_name.variable_name

Example:

print object.varabl

Accessing Attributes

Object attributes can also be accessed by using dot operator.
Example:

stud1.display()
stud2.display()

print " total number of students are: %d" %  student.i

Use Of Pre-defined Functions

Instead of using general statements to access attributes, programmers can use the following functions:

    getattr( obj, name [,default] ) : used to access object’s attribute.

    hasattr( object, name): used for checking whether the attribute exists or not.

    setattr( obj, name, value ) : set or create an attribute, if doesn’t exist.

    delattr( obj, name ) : used to delete an attribute.

Built-In Class Attributes

All the Python built-in class attributes can be accessed using dot (.) operator like other attributes.

The built-in class attributes are:

    __dict__: This attribute is a dictionary that contains class’s-namespace.
    __doc__: Used for class documentation string.
    __name__: used as class-name.
    __module__: used to define module name for the class in which it is defined. In interactive mode it is __main__.
    __bases__: An empty tuple containing the base-class.
