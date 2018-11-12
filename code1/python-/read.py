import sys

list = ['item1', 'item2', 'item3']

def show():
    with open("test.txt") as file:
        for line in file:
            print(line)


show()
