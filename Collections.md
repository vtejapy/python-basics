# Collections

## List
   * Lists are a container data type that acts as a dynamic array. 
   * The Python list type is called list. It is a type of sequence – we can use it to store multiple values, and access them sequentially, by their position, or index, in the list. We define a list literal by putting a comma-separated list of values inside square brackets ([ and ]):
   * A list has a (current) length -- Get the length of a list with len(mylist).
   * A list has an order -- The items in a list are ordered, and you can think of that order as going from left to right.
   * A list is heterogeneous -- You can insert different types of objects into the same list.
   * Lists are mutable, 

```
# a list of strings
animals = ['cat', 'dog', 'fish', 'bison']

# a list of integers
numbers = [1, 7, 34, 20, 12]

# an empty list
my_list = []

# a list of variables we defined somewhere else
things = [
    one_variable,
    another_variable,
    third_variable]
```

eg:
```
>>> l = [1, 2, 3]
>>> l[0]
1
>>> l.append(1)
>>> l
[1, 2, 3, 1]
```

## Built in methods in List
### Difference between append() and extend()

Lists have several methods amongst which the append() and extend() methods. The former appends an object to the end of the list (e.g., another list) while the later appends each element of the iterable object (e.g., anothee list) to the end of the list.

For example, we can append an object (here the character ‘c’) to the end of a simple list as follows:
```
>>> stack = ['a','b']
>>> stack.append('c')
>>> stack
['a', 'b', 'c']
```
However, if we want to append several objects contained in a list, the result as expected (or not...) is:
```
>>> stack.append(['d', 'e', 'f'])
>>> stack
['a', 'b', 'c', ['d', 'e', 'f']]
```

The object ['d', 'e', 'f'] has been appended to the exiistng list. However, it happens that sometimes what we want is to append the elements one by one of a given list rather the list itself. You can do that manually of course, but a better solution is to use the extend() method as follows:
```
>>> stack = ['a', 'b', 'c']
>>> stack.extend(['d', 'e','f'])
>>> stack
['a', 'b', 'c', 'd', 'e', 'f']
```
## Other list methods
### index
The index() methods searches for an element in a list. For instance:
```
>>> my_list = ['a','b','c','b', 'a']
>>> my_list.index('b')
1
```
It returns the index of the first and only occurence of ‘b’. If you want to specify a range of valid index, you can indicate the start and stop indices:
```
>>> my_list = ['a','b','c','b', 'a']
>>> my_list.index('b', 2)
3
```
Warning

if the element is not found, an error is raised

### insert
You can remove element but also insert element wherever you want in a list:
```
>>> my_list.insert(2, 'a')
>>> my_list
['b', 'c', 'a', 'b']
```
The insert() methods insert an object before the index provided.

### remove
Similarly, you can remove the first occurence of an element as follows:
```
>>> my_list.remove('a')
>>> my_list
['b', 'c', 'b', 'a']
```
### pop
Or remove the last element of a list by using:
```
>>> my_list.pop()
'a'
>>> my_list
['b', 'c', 'b']
````
which also returns the value that has been removed.

### count
You can count the number of element of a kind:
```
>>> my_list.count('b')
2
```
### sort
There is a sort() method that performs an in-place sorting:
```
>>> my_list.sort()
>>> my_list
['a', 'b', 'b', 'c']
```

There is also the possiblity to sort in the reverse order:
```
>>> my_list.sort(reverse=True)
>>> my_list
['c', 'b', 'b', 'a']
```
### reverse
Finally, you can reverse the element in-place:
```
>>> my_list = ['a', 'c' ,'b']
>>> my_list.reverse()
>>> my_list
['b', 'c', 'a']
```
### Operators
The + operator can be used to extend a list:
```
>>> my_list = [1]
>>> my_list += [2]
>>> my_list
[1, 2]
>>> my_list += [3, 4]
>>> my_list
[1, 2, 3, 4]
```

The * operator ease the creation of list with similar values

```
>>> my_list = [1, 2]
>>> my_list = my_list * 2
>>> my_list
[1, 2, 1, 2]
```
### Slicing
Slicing uses the symbol : to access to part of a list:
```
>>> list[first index:last index:step]
>>> list[:]
>>> a = [0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5]
>>> a[2:]
[2, 3, 4, 5]
>>> a[:2]
[0, 1]
>>> a[2:-1]
[2, 3, 4]
```
By default the first index is 0, the last index is the last one..., and the step is 1. The step is optional. So the following slicing are equivalent:
```
>>> a = [1, 2, 3, 4, 5, 6, 7, 8]
>>> a[:]
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a[::1]
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a[0::1]
[1, 2, 3, 4, 5, 6, 7, 8]
```
### List comprehension
Traditionally, a piece of code that loops over a sequence could be written as follows:
```
>>> evens = []
>>> for i in range(10):
...     if i % 2 == 0:
...         evens.append(i)
>>> evens
[0, 2, 4, 6, 8]
```
This may work, but it actually makes things slower for Python because the interpreter works on each loop to determine what part of the sequence has to be changed.

A list comprehension is the correct answer:
```
>>> [i for i in range(10) if i % 2 == 0]
[0, 2, 4, 6, 8]
```
Besides the fact that it is more efficient, it is also shorter and involves fewer elements.

### Filtering Lists
```
>>> li = [1, 2]
>>> [elem*2 for elem in li if elem>1]
[4]
```
### Lists as Stacks
The Python documentation gives an example of how to use lists as stacks, that is a last-in, first-out data structures (LIFO).

An item can be added to a list by using the append() method. The last item can be removed from the list by using the pop() method without passing any index to it.
```
>>> stack = ['a','b','c','d']
>>> stack.append('e')
>>> stack.append('f')
>>> stack
['a', 'b', 'c', 'd', 'e', 'f']
>>> stack.pop()
'f'
>>> stack
['a, 'b', 'c', 'd', 'e']
```
### Lists as Queues
Another usage of list, again presented in Python documentation is to use lists as queues, that is a first in - first out (FIFO).
```
>>> queue = ['a', 'b', 'c', 'd']
>>> queue.append('e')
>>> queue.append('f')
>>> queue
['a', 'b', 'c', 'd', 'e', 'f']
>>> queue.pop(0)
'a'
```
### How to copy a list
There are three ways to copy a list:
```
>>> l2 = list(l)
>>> l2 = l[:]
>>> import copy
>>> l2 = copy.copy(l)
```
Warning
Don’t do l2 = l, which is a reference, not a copy.
The preceding techniques for copying a list create shallow copies. IT means that nested objects will not be copied. Consider this example:
```
>>> a = [1, 2, [3, 4]]
>>> b = a[:]
>>> a[2][0] = 10
>>> a
[1, 2, [10, 4]]
>>> b
[1, 2, [10, 4]]
```
To get around this problem, you must perform a deep copy:
```
>>> import copy
>>> a = [1, 2, [3, 4]]
>>> b = copy.deepcopy(a)
>>> a[2][0] = 10
>>> a
[1, 2, [10, 4]]
>>> b
[1, 2, [3, 4]]
```
### Inserting items into a sorted list
The bisect module provides tools to manipulate sorted lists.
```
>>> x = [4, 1]
>>> x.sort()
>>> import bisect
>>> bisect.insort(x, 2)
>>> x
[1, 2, 4]
```
To know where the index where the value would have been inserted, you could have use:
```
>>> x = [4, 1]
>>> x.sort()
>>> import bisect
>>> bisect.bisect(x, 2)
2

```


# Tuples
In Python, tuples are part of the standard language. This is a data structure very similar to the list data structure. The main difference being that tuple manipulation are faster than list because tuples are immutable.

## Constructing tuples
To create a tuple, place values within brackets:
```
>>> l = (1, 2, 3)
>>> l[0]
1
```
It is also possible to create a tuple without parentheses, by using commas:
```
>>> l = 1, 2
>>> l
(1, 2)
```
If you want to create a tuple with a single element, you must use the comma:
```
>>> singleton = (1, )
```
You can repeat a tuples by multiplying a tuple by a number:
```
>>> (1,) * 5
(1, 1, 1, 1, 1)
```
Note that you can concatenate tuples and use augmented assignement (*=, +=):
```
>>> s1 = (1,0)
>>> s1 += (1,)
>>> s1
(1, 0, 1)
```
## Tuple methods
Tuples are optimised, which makes them very simple objects. There are two methods available only:

index, to find occurence of a value
count, to count the number of occurence of a value
```
>>> l = (1,2,3,1)
>>> l.count(1)
2
>>> l.index(2)
1
```
## Interests of tuples
So, Tuples are useful because there are

faster than lists
protect the data, which is immutable
tuples can be used as keys on dictionaries
In addition, it can be used in different useful ways:

## Tuples as key/value pairs to build dictionaries
```
>>> d = dict([('jan', 1), ('feb', 2), ('march', 3)])
>>> d['feb']
2
```

## signing multiple values
```
>>> (x,y,z) = ('a','b','c')
>>> x
'a'
>>> (x,y,z) = range(3)
>>> x
0
```
## Tuple Unpacking
Tuple unpacking allows to extract tuple elements automatically is the list of variables on the left has the same number of elements as the length of the tuple
```
>>> data  = (1,2,3)
>>> x, y, z = data
>>> x
1
```
## Tuple can be use as swap function
This code reverses the contents of 2 variables x and y:
```
>>> (x,y) = (y,x)
```
Warning
Consider the following function:
```
def swap(a, b):
    (b, a) = (a, b)
```
then:
```
a = 2
b = 3
swap(a, b)
#a is still 2 and b still 3 !! a and b are indeed passed by value not reference.
```

## length
To find the length of a tuple, you can use the len() function:
```
>>> t= (1,2)
>>> len(t)
2
```
## Slicing (extracting a segment)
```
>>> t = (1,2,3,4,5)
>>> t[2:]
(3, 4, 5)
```
## Copy a tuple
To copy a tuple, just use the assignement:
```
>>> t = (1, 2, 3, 4, 5)
>>> newt = t
>>> t[0] = 5
>>> newt
(1, 2, 3, 4, 5)
```
Warning

You cannot copy a list with the = sign because lists are mutables. The = sign creates a reference not a copy. Tuples are immutable therefore a = sign does not create a reference but a copy as expected.

## Tuple are not fully immutable !!
If a value within a tuple is mutable, then you can change it:
```
>>> t = (1, 2, [3, 10])
>>> t[2][0] = 9
>>> t
(1, 2, [9, 10])
```
## Convert a tuple to a string
You can convert a tuple to a string with either:
```
>>> str(t)
or

>>> `t`
```
## math and comparison
comparison operators and mathematical functions can be used on tuples. Here are some examples:
```
>>> t = (1, 2, 3)
>>> max(t)
3
```


# Dicts
A dictionary is a sequence of items. Each item is a pair made of a key and a value. Dictionaries are not sorted. You can access to the list of keys or values independently.
```
>>> d = {'first':'string value', 'second':[1,2]}
>>> d.keys()
['first', 'second']
>>> d.values()
['string value', [1, 2]]
```
You can access to the value of a given key as follows:
```
>>> d['first']
'string value'
```
Warning
You can not have duplicate keys in a dictionary
dictionary have no concept of order among elements

## Methods to query information
In addition to keys and values methods, there is also the items method that returns a list of items of the form (key, value). The items are not returned in any particular order:
```
>>> d = {'first':'string value', 'second':[1,2]}
>>> d.items()
[('a', 'string value'), ('b', [1, 2])]
```
The iteritems method works in much the same way, but returns an iterator instead of a list. See iterators section for an example.
You can check for the existence of a specific key with has_key:
```
>>> d.has_key('first')
True
```
The expression d.has_key(k) is equivalent to k in d. The choice of which to use is largely a matter of taste.

In order to get the value corresponding to a specific key, use get or pop:
```
>>> d.get('first')  # this method can set an optional value, if the key is not found
'string value'
```
It is useful for things like adding up numbers:
```
sum[value] = sum.get(value, 0) + 1
```
## setdefault, collections

The difference between get and pop is that pop also removes the corresponding item from the dictionary:
```
>>> d.pop('first')
'string value'
>>> d
{'second': [1, 2]}
```
Finally, popitem removes and returns a pair (key, value); you do not choose which one because a dictionary is not sorted
```
>>> d.popitem()
('a', 'string value')
>>> d
{'second': [1, 2]}

```
## Methods to create new dictionary
Since dictionaries (like other sequences) are objects, you should be careful when using the affectation sign:
```
>>> d1 = {'a': [1,2]}
>>> d2 = d1
>>> d2['a'] = [1,2,3,4]
>>> d1['a]
[1,2,3,4]
```
To create a new object, use the copy method (shallow copy):
```
>>> d2 = d1.copy()
```
See also
```
copy.deepcopy()
```
You can clear a dictionary (i.e., remove all its items) using the clear() method:
```
>>> d2.clear()
{}
```
The clear() method deletes all items whereas del() deletes just one:
```
>>> d = {'a':1, 'b':2, 'c':3}
>>> del d['a']
>>> d.clear()
```
Create a new item with default value (if not provided, None is the default):
```
>>> d2.setdefault('third', '')
>>> d2['third']
''
```
Create a dictionary given a set of keys:
```
>>> d2.fromkeys(['first', 'second'])
```
another syntax is to start from an empty dictionary:
```
>>> {}.fromkeys(['first', 'second'])
{'first': None, 'second': None}
```
Just keep in ,ind thqt the fromkeys() method creates a new dictionary with the given keys, each with a default corresponding value of None.

## Combining dictionaries
Given 2 dictionaries d1 and d2, you can add all pairs of key/value from d2 into d1 by using the update method (instead of looping and assigning each pair yourself:
```
>>> d1 = {'a':1}
>>> d2 = {'a':2; 'b':2}
>>> d1.update(d2)
>>> d1['a']
2
>>> d2['b']
2
```
The items in the supplied dictionary are added to the old one, overwriting any items there with the same keys.

## iterators
Dictionary provides iterators over values, keys or items:
```
>>> [x for x in t.itervalues()]
['string value', [1, 2]]
>>>
>>> [x for x in t.iterkeys()]
['first', 'csecond']
>>> [x for x in t.iteritems()]
[('a', 'string value'), ('b', [1, 2])]
```
## Views
viewkeys, viewvalues, viewitems are set-like objects providing a view on D’s keys, values or items.

# comparison
you can compare dictionaries! Python first compares the sorted key-value pairs. It first sorts dictionaries by key and comapre their initial items. If the items hae different values, Python figures out the comparison between them. Otherwise, the second items are compared and so on.



## Sets

Sets are constructed from a sequence (or some other iterable object). Since sets cannot have duplicated, there are usually used to build sequence of unique items (e.g., set of identifiers).
```
4.5.1. Quick example
>>> a = set([1, 2, 3, 4])
>>> b = set([3, 4, 5, 6])
>>> a | b # Union
{1, 2, 3, 4, 5, 6}
>>> a & b # Intersection
{3, 4}
>>> a < b # Subset
False
>>> a - b # Difference
{1, 2}
>>> a ^ b # Symmetric Difference
{1, 2, 5, 6}
```
Note

the intersection, subset, difference and symmetric difference can be be called with method rather that symbols. See below for examples.

## Ordering
Just as with dictionaries, the ordering of set elements is quite arbitrary, and shouldn’t be relied on.

## Operators
As mentionned in the quick example section, each operator is associated to a symbol (e.g., &) and a method name (e.g. union).
```
>>> a = set([1, 2, 3])
>>> b = set([2, 3, 4])
>>> c = a.intersection(b) # equivalent to c = a & b
>>> a.intersection(b)
set([2, 3])
>>> c.issubset(a)
True
>>> c <= a
True
>>> c.issuperset(a)
False
>>> c >= a
False
>>> a.difference(b)
set([1])
>>> a - b
set([1])
>>> a.symmetric_difference(b)
set([1, 4])
>>> a ^ b
set([1, 4])
```
You can also copy a set using the copy method:
```
>>> a.copy()
set([1, 2, 3])
```

Frozensets
Sets are mutable, and may therefore not be used, for example, as keys in dictionaries.

Another problem is that sets themselves may only contain immutable (hashable) values, and thus may not contain other sets.

Because sets of sets often occur in practice, there is the frozenset type, which represents immutable (and, therefore, hashable) sets.

Quick Example
```
>>> a = frozenset([1, 2, 3])
>>> b = frozenset([2, 3, 4])
>>> a.union(b)
frozenset([1, 2, 3, 4])
```
## Set of Sets
Sets may only contain immutable (hashable) values, and thus may not contain other sets, in which case frozensets can be useful. Consider the following example:
```
>>> a = set([1, 2, 3])
>>> b = set([2, 3, 4])
>>> a.add(b)
>>> a.add(frozenset(b))
```
## Using set as key in a dictionary¶
If you want to use a set as a key dictionary, you will need frozenset:
```
>>> fa = {frozenset([1,2]): 1}
>>> fa[ frozenset([1,2]) ]
1
```
### Methods
frozensets have less methods than sets.
There are some operators similar to sets (intersection(), union(), symmetric_difference(), difference(), issubset(), isdisjoint(), issuperset()) and a copy() method.

