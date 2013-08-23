#!/usr/bin/env python

def find_element(alist,value):
    i = 0
    for e in alist:
        if e == value:
            return i
        i += 1
    return - 1


print find_element([1,2,3],3)
print find_element(['alpha','beta'],'gamma')

