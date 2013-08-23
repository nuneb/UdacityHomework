#!/usr/bin/env python

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


a = [1,2,3]
b = [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]
#print b
#>>> [2,4,6]

