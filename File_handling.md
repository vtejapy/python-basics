# File handling
A file is some information or data which stays in the computer storage devices. 

File opening

To open a file we use open() function. It requires two arguments, first the file path or file name, second which mode it should open. Modes are like

* “r” -> open read only, you can read the file but can not edit / delete anything inside
* “w” -> open with write power, means if the file exists then delete all content and open it to write
* “a” -> open in append mode

The default mode is read only, ie if you do not provide any mode it will open the file as read only. Let us open a file
```
>>> fobj = open("love.txt")
>>> fobj
<_io.TextIOWrapper name='love.txt' mode='r' encoding='UTF-8'>
```
## Closing a file

After opening a file one should always close the opened file. We use method close() for this.
```
>>> fobj = open("love.txt")
>>> fobj
<_io.TextIOWrapper name='love.txt' mode='r' encoding='UTF-8'>
>>> fobj.close()
```

To read the whole file at once use the read() method.
```
>>> fobj = open("sample.txt")
>>> fobj.read()
'I love Python\nPradeepto loves KDE\nSankarshan loves Openoffice\n'
```
If you call read() again it will return empty string as it already read the whole file. readline() can help you to read one line each time from the file.
```
>>> fobj = open("sample.txt")
>>> fobj.readline()
'I love Python\n'
>>> fobj.readline()
'Pradeepto loves KDE\n'
```
To read all the lines in a list we use readlines() method.
```
>>> fobj = open("sample.txt")
>>> fobj.readlines()
['I love Python\n', 'Pradeepto loves KDE\n', 'Sankarshan loves Openoffice\n']
```
You can even loop through the lines in a file object.
```
>>> fobj = open("sample.txt")
>>> for x in fobj:
...     print(x,)
...
I love Python
Pradeepto loves KDE
Sankarshan loves Openoffice
```
Let us write a program which will take the file name as the input from the user and show the content of the file in the console.

```
name = input("Enter the file name: ")
fobj = open(name)
print(fobj.read())
fobj.close()
```
In the last line you can see that we closed the file object with the help of close() method.

The output
```
$ ./showfile.py
Enter the filename: sample.txt
I love Python
Pradeepto loves KDE
Sankarshan loves Openoffice
```
### Using the with statement

In real life scenarios we should try to use with statement. It will take care of closing the file for you.
```
>>> with open('setup.py') as fobj:
...     for line in fobj:
...         print line,
...
```
### Writing in a file

Let us open a file then we will write some random text into it by using the write() method.
```
>>> fobj = open("ircnicks.txt", 'w')
>>> fobj.write('powerpork\n')
>>> fobj.write('indrag\n')
>>> fobj.write('mishti\n')
>>> fobj.write('sankarshan')
>>> fobj.close()
```
Now read the file we just created
```
>>>fobj = open('ircnicks.txt')
>>> s = fobj.read()
>>> print(s)
powerpork
indrag
mishti
sankarshan

```
