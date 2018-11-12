import sys
import requests

#open file
with open("abc.txt") as file:
    #loop through file and print out json response
    for line in file:
        r = requests.get(line)
        print(line)
        if r.ok:
            print(r.json())
        else:
            print(r.ok)
            print('niet gelukt')
