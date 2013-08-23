#!/usr/bin/env python

#def find_element(p,t):
#    i = 0
#    for e in p:
#        if e == t:
#            return i
#        i = i + 1
#    return -1

#def find_element(p,t):
#    i = 0
#    while i < len(p):
#        if p[i] == t:
#            return i
#        i = i + 1
#    return -1


def find_element(p,t):
    if t in p:
        return p.index(t)
    else:
        return -1


print find_element([1,2,3],3)
print find_element(['alpha','beta'],'gamma')

