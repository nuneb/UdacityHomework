#!/usr/bin/env python

i = 0
while i < 5:
    print i
    i = i + 1
print 'BOOM'

i = 0
while i != 4:
    i = i + 1
    print i
print 'Boom' * 5

def print_numbers(n):
    i = 1
    while i <= n:
        print i
        i = i + 1
print print_numbers(10)

def countdown(a):
    i = 1
    while a > 0:
        print a 
        a = a - 1
    print 'Blastoff!'
print countdown(3)

