# Iteration

## For 

Iterate over a sequence or an "iterable" object.
  * Sequences and containers are iterable. Examples: tuples, lists, strings, dictionaries.

syntax:

```
for variable in sequence:
  Statement1
  Statement2  
  ...
  
```

```
>>> a = ['Fedora', 'is', 'powerful']
>>> for x in a:
...     print(x)
...
Fedora
is
powerful
```

```
>>> a = [1, 2, 3, 4, 5]
>>> for x in a:
...     print(x)
1
2
3
4
5
```

```
>>> languages = ["C", "C++", "Perl", "Python"] 
>>> for x in languages:
...     print x
... 
C
C++
Perl
Python
>>> 
```

## The range() Function

The built-in function range() is the right function to iterate over a sequence of numbers

range(n)

```
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

range(begin,end)

```
>>> range(1,5)
[1, 2, 3, 4]

```

range(begin,end, step)
```
>>> range(4,50,5)
[4, 9, 14, 19, 24, 29, 34, 39, 44, 49]
```

eg-2:

```
n = 101
sum = 0
for i in range(1,n):
    sum = sum + i
print sum
```


## While loop

The while statement allows you to repeatedly execute a block of statements as long as a condition is true. 

The syntax for while statement is like

```
while condition:
    statement1
    statement2
```

eg:

```
>>> n = 0
>>> while n < 11:
...     print(n)
...     n += 1
...
0
1
2
3
4
5
6
7
8
9
10
````


## Loop Control Statements

### Break statement

It is used to exit a while loop or a for loop. It terminates the looping & transfers execution to the statement next to the loop.

```
#!/usr/bin/python

count = 0

while count <= 100: print (count) count += 1 if count >= 3 :
      break
```

output:

```
0
1
2
```

### Continue statement  
It causes the looping to skip the rest part of its body & start re-testing its condition.

```
#!/usr/bin/python

for x in range(10):
   #check whether x is even
   if x % 2 == 0:
      continue
   print x

```

output:
```
1
3
5
7
9
```

### Pass Statement

It is used in Python to when a statement is required syntactically and the programmer does not want to execute any code block or command.

```
for letter in 'TutorialsCloud': 
   if letter == 'C':
      pass
      print 'Pass block'
   print 'Current letter is:', letter
```
Output:
```
Current letter is : T
Current letter is : u
Current letter is : t
Current letter is : o
Current letter is : r
Current letter is : i
Current letter is : a
Current letter is : l
Current letter is : s
Pass block
Current letter is : C
Current letter is : l
Current letter is : o
Current letter is : u
Current letter is : d
```
