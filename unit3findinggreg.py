#!/usr/bin/env python

def find_element(alist,value):
    for index in range(len(alist)):
        element = alist[index]
        if element == value:
            return index
    return - 1
    



print find_element([1,2,3],3)
print find_element(['alpha','beta'],'gamma')
