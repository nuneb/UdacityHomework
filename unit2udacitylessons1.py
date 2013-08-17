#!/usr/bin/env python

def square(x):
    return x * x
print square(9)

def sum(a, b):
    a = a + b
    return a
print sum('N', 'B')

def abbaize(a, b):
    return a + b + b + a

x = 1
y = 2

print abbaize(x,y)
print abbaize('a','b')
#>>> 'abba'

print abbaize('dog','cat')
#>>> 'dogcatcatdog'

def find_second(start, target):
    first_target = start.find(target)
    return start.find(target, first_target +1)
# return start.find(target, start.find(target) + 1)

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')

twister = "she sells seashells by the seashore"
print find_second(twister,'she')
