# Classes
Classes model the behavior of objects in the "real" world. Methods implement the behaviors of these types of objects. Member variables hold (current) state. Classes enable us to implement new data types in Python.

The `class:` statement is used to define a class. The `class:` statement creates a class object and binds it to a name.
A simple class

```
class A:
    pass

a = A()
```

To define a new style class (recommended), inherit from object or from another class that does. Example:
```
class A(object):
pass


a = A()
a
<__main__.A object at 0x82fbfcc>
```
## Defining methods
A method is a function defined in class scope and with first parameter self:

```
class B(object):
     def show(self):
         print 'hello from B'

b = B()
b.show()
hello from B
```
A method as we describe it here is more properly called an instance method, in order to distinguish it from class methods and static methods.

## The constructor

The constructor is a method named __init__.

```
class A(object):
       def __init__(self, name):
           self.name = name
       def show(self):
           print 'name: "%s"' % self.name

a = A('dave')
a.show()
name: "dave"
```

Notes:

    The self variable is explicit. It references the current object, that is the object whose method is currently executing.
    The spelling ("self") is optional, but everyone spells it that way.

## Member variables

Defining member variables -- Member variables are created with assignment. Example:

```
class A(object):
    def __init__(self, name):
        self.name = name
```
A small gotcha -- Do this:
```
class A(object):
     def __init__(self, items=None):
         if items is None:
             self.items = []
         else:
             self.items = items
```
Do not do this:
```
 class B:
        def __init__(self, items=[]):   # wrong.  list ctor evaluated only once.
            self.items = items

```

In the second example, the def statement and the list constructor are evaluated only once. Therefore, the item member variable of all instances of class B, will share the same value, which is most likely not what you want.


## Calling methods
   * Use the instance and the dot operator.
   * Calling a method defined in the same class or a superclass:
   * From outside the class -- Use the instance:

```
        some_object.some_method()
        an_array_of_of_objects[1].another_method()
```
From within the same class -- Use self:

```
        self.a_method()
```
From with a subclass when the method is in the superclass and there is a method with the same name in the current class -- Use the class (name) or use super:

```
        SomeSuperClass.__init__(self, arg1, arg2) super(CurrentClass,
        self).__init__(arg1, arg2)
```
Calling a method defined in a specific superclass -- Use the class (name).

## Class variables

   * Also called static data.

   * A class variable is shared by instances of the class.

Define at class level with assignment. Example:

```
    class A(object):
        size = 5
        def get_size(self):
            return A.size
```
    Reference with classname.variable.
```
    Caution: self.variable = x creates a new member variable.
```
## Class methods and static methods

### Instance (plain) methods:

    An instance method receives the instance as its first argument.

### Class methods:
    * A class method receives the class as its first argument.
    * Define class methods with built-in function classmethod() or with decorator @classmethod.
    * See the description of classmethod() built-in function at "Built-in Functions": http://docs.python.org/2/library/functions.html#classmethod

```
class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
fun: function that needs to be converted into a class method
returns: a class method for function.
```

###Static methods:
   * A static method receives neither the instance nor the class as its first argument.
   * Define static methods with built-in function staticmethod() or with decorator @staticmethod.
   * See the description of staticmethod() built-in function at "Built-in Functions": http://docs.python.org/2/library/functions.html#staticmethod

```
class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
        ...
returns: a static method for function fun.

```


## Inheritance

In order to inherit fro, an existing class, use the following syntax:
```
class Animal(object):
    def __init__(self, name="unknown"):
        self.name = name
    def __str__(self):
        print("I'm a {0}".format(self.name))

def Cat(Animal):
    def __init__(self):
        super().__init__(name='CAT')
```
Here, the parent’s class Animal is initialised inside the child class using the super keyword. The Cat inherits from Animal and therefore has the method print already available.
## Multiple inheritance

if Python cannot find a variable or method in the local namespace, it will perform a depth first search of the super classes in the same order in which the superclasses are specified in the class definition.

That’s all you need to know !! Let us study an example:
```
class Vehicle(object):
    def __init__(self, name, color, wheel):
        self.name = name
        self.wheels = None
        self.color = None

    def set_wheels(self, n):
          self.wheels = 2

    def __str__(self):
        txt = str(self.name) + ":" + registration
        return txt

class TwoWheeler(object):

    def __init__(self, name, color):
        self.name = name
        self.set_wheels(2)
        self.color = None

    def __str__(self):
        return  self.wheels

class MotorVehicle(object):

    def __init__(self, name, color, power):
        self.name = name
        self.set_wheels(2)
        self.color = None
        self.power

class Bicycle(TwoWheeler, gear):

    def __init__(self, name, color, gear):
        self.name = name
        self.set_wheels(2)
        self.color = None
```


## property

The property built-in function enables us to write classes in a way that does not require a user of the class to use getters and setters. Example:

```
class Person:
    def __init__(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

jane = Person(153) # Jane is 153cm tall

jane.height += 1 # Jane grows by a centimetre
jane.set_height(jane.height + 1) # Jane grows again

```

The property built-in function is also a decorator. So, the following is equivalent to the above example:

```
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return "%s %s" % (self.name, self.surname)

    @fullname.setter
    def fullname(self, value):
        # this is much more complicated in real life
        name, surname = value.split(" ", 1)
        self.name = name
        self.surname = surname

    @fullname.deleter
    def fullname(self):
        del self.name
        del self.surname

jane = Person("Jane", "Smith")
print(jane.fullname)

jane.fullname = "Jane Doe"
print(jane.fullname)
print(jane.name)
print(jane.surname)

```

