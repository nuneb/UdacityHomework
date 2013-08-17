#!/usr/bin/env python
def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    big = biggest(a,b,c)
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
    else:
        return bigger(a,b)

def small(a,b):
    if a < b:
        return a
    else:
        return b

def smallest(a,b,c):
    return small(a,small(b,c))

def set_range(a,b,c):
    return biggest(a,b,c) - smallest(a,b,c)


print set_range(10, 4, 7)


#print(median(1,2,3))
#>>> 2
#print(median(9,3,6))
#>>> 6
#print(median(7,8,7))
#>>> 7





