#!/usr/bin/env python

def bad_hash_string(keyword,buckets):
    return ord(keyword[0]) % buckets

def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        hv = func(w,size)
        results[hv] += 1
        keys_used.append(w)
    return results

#.split() and then len(words)

def hash_string(keyword, buckets):
    for char in keyword:
        location = ord(char) % buckets
    
