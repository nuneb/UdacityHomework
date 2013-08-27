#!/usr/bin/env python

def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        hv = func(w,size)
        results[hv] += 1
        keys_used.append(w)
    return results

def hash_string(keyword, buckets):
    location = 0
    for char in keyword:
        location = (location + ord(char)) % buckets
    return location

print hash_string('a',12)
#>>> 1
print hash_string('b',12)
#>>> 2
print hash_string('a',13)
#>>> 6
print hash_string('au',12)
#>>> 10
print hash_string('udacity',12)
#>>> 11


# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

#def make_hashtable(nbuckets):
#    i = 0
#    table = []
#    while i < nbuckets:
#        table.append([])
#        i = i + 1
#    return table

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

# Define a procedure, hashtable_get_bucket,
# that takes two inputs - a hashtable, and
# a keyword, and returns the bucket where the
# keyword could occur.

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key,len(htable))]


table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]
print hashtable_get_bucket(table, "Zoe")
#>>> [['Bill', 17], ['Zoe', 14]]
print hashtable_get_bucket(table, "Brick")
#>>> []
print hashtable_get_bucket(table, "Lilith")
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]

def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable, key).append([key, value])
    return htable

table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]], 
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]


# Define a procedure,
# hashtable_lookup(htable,key)
# that takes two inputs, a hashtable
# and a key (string), and returns the
# value associated with that key.

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

print hashtable_lookup(table, 'Francis')
#>>> 13
print hashtable_lookup(table, 'Louis')
#>>> 29
print hashtable_lookup(table, 'Zoe')
#>>> 14


# Define a procedure,
# hashtable_update(htable,key,value)
# that updates the value associated with key. If key is already in the
# table, change the value to the new value. Otherwise, add a new entry
# for the key and value.

# Hint: Use hashtable_lookup as a starting point.
# Make sure that you return the new htable

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry.pop()
            entry.append(value)
    return htable

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42], 
#>>> ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2], 
#>>> ['Rochelle', 94]]]