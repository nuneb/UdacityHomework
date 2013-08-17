#!/usr/bin/env python

# Define a procedure, sum_list, that takes as its input a
# list of numbers, and returns the sum of all the elements in
# the input list.

def sum_list(list):
    for i in list:
        return list[0] + list[1] + list[2]

#professor's answer
#def sum_list(p):
#    result = 0
#    for e in p:
#        result = result + e
#    return result
    

print sum_list([1, 7, 4])
#>>> 12
print sum_list([9, 4, 10])
#>>> 23
print sum_list([44, 14, 76])
#>>> 134

# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.
def measure_udacity(p):
    s = 'U'
    for s in p:
        return p
    
print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0
print measure_udacity(['Umika','Umberto'])
#>>> 2