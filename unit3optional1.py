#!/usr/bin/env python

def list_test(n,m,o):
    n.append('a')
    m += ['a','b','c']
    return o + ['w']

first_input = [1,2,3]
second_input = [4,5,6]
third_input = [7,8,9]

print list_test(first_input, second_input, third_input)
#>>> [7,8,9,'w']
print first_input
#>>> [1,2,3,'a']
print second_input
#>>> [4,5,6,'a','b','c']
print third_input
#>>> [7,8,9]

def symmetric(p):
    i=0
    while i < len(p):
        row = p[i]
        column = [p[0][i]]
        j = 1
        while j < len(p):
            column.append(p[j][i])
            j += 1
        if column != row:
            return False
        i += 1
    return True

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False



def list_mean(n):
    if n == []:
        return 0
    i = 0
    for e in n:
        i += 1.
        count = i
    result = 0
    for e in n:
        result = result + e
    total = result
    return result / count

print list_mean([1,2,3,4])
print list_mean([1,3,4,5,2])
print list_mean([])
print list_mean([2])

