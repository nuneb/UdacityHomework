#!/usr/bin/env python

def print_multiplication_table(n):
    i = 1
    while i <= n:
        j = i 
        while j <= n:
            print str(i) + ' * ' + str(j) + ' = ' + str(i*j)
            j = j + 1
        i = i + 1
        
print print_multiplication_table(12)
