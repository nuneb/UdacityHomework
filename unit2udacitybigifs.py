#!/usr/bin/env python

def bigger(x, y):
    if x > y:
        return x
    elif x == y:
        return x
    else:
        return y

print bigger(2,7)
#>>> 7
print bigger(3,2)
#>>> 3
print bigger(3,3)
#>>> 3

def is_friend(name):
    if name[0] == 'D' or name[0] == 'N':
        return True
    else:
        return False

print is_friend('Diane')
#>>> True
print is_friend('Ned')
#>>> True
print is_friend('Moe')
#>>> False


def biggest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= a and c >= b:
        return c
# Use bigger
# return bigger(bigger(a, b), c)

print biggest(3, 6, 9)
#>>> 9
print biggest(6, 9, 3)
#>>> 9
print biggest(9, 3, 6)
#>>> 9
print biggest(3, 3, 9)
#>>> 9
print biggest(9, 3, 9)
#>>> 9


def print_numbers(n):
    i = 1
    while i <= n:
        print i
        i = i + 1
print print_numbers(3)





