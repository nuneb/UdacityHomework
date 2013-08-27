#!/usr/bin/env python
# unit 3 problemset

p = [0,1,1]
p[0] = p[0] + p[1]
p[1] = p[0] + p[2]
p[2] = p[0] + p[1]
print p
print
# Define a procedure, product_list,
# takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(p):
    total = 1
    for i in p:
        total = total * i
    return total

print product_list([9])
#>>> 9
print product_list([1,2,3,4])
#>>> 24
print product_list([])
#>>> 1
print
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(g):
    big = 0
    for i in g:
        if i > big:
            big = i
    return big
print greatest([4,23,1])    #>>> 23
print greatest([])          #>>> 0
print
# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.
# The procedure should return two numbers, not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(u):
    students = 0
    tuition = 0
    for name, student, price in u:
        students = students + student
        tuition = tuition + (student * price)
    return students, tuition

print total_enrollment(udacious_univs)  #>>> (90000,0)
# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside 
# interpreter you might not see it.
print total_enrollment(usa_univs)       #>>> (77285,3058581079L)
    



