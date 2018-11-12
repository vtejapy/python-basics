import sys

list = ['item1', 'item2', 'item3']

def remember():
    #open file
    file = open("test.txt", "a")
    for item in list:
        file.write(item+"\n")

remember()
