#!/usr/bin/env python

# Given the variable countries defined as:
#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]
# Write code to print out the capital of India
# by accessing the array.
print countries[1][1]
print countries[0][2] / countries[2][2]

# We defined:
stooges = ['Moe','Larry','Curly']
# but in some Stooges films, Curly was
# replaced by Shemp.
# Write one line of code that changes
# the value of stooges to be:
['Moe','Larry','Shemp']
# but does not create a new List
# object.
stooges[2] = 'Shemp'
print stooges

# Define a procedure, replace_spy, that takes as its input a list of
# three numbers, and modifies the value of the third element in the
# input list to be one more than its previous value.
spy = [0,0,7]
def replace_spy(p):
    p[2] = p[2] + 1
# In the test below, the first line calls your procedure which will change spy, and the 
# second checks you have changed it.
replace_spy(spy)
print spy
#>>> [0,0,8]

speed_of_light = 299792458.   # meters per second
meter = 1
kilometer = 1000
nanosecond = 1.0/1000000000  # one billionth of a second
millasecond = 1.0/1000000
cycles_per_second = 2700000000.0 #2.7 GHz

cycle_distance = speed_of_light / cycles_per_second

print speed_of_light / kilometer
print speed_of_light * (0.4 * nanosecond)
print speed_of_light * (12 * nanosecond)
print speed_of_light * (7 * millasecond)

bit = 8.79609e12
dollar_per_bit = 100 / bit
nanodollar = 1/1000000000.

print dollar_per_bit / nanodollar
