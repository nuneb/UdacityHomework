#!/usr/bin/env python

def find_last(search, target):
    last_pos = -1
    while True:
        pos = search.find(target, last_pos + 1)
        if pos == -1:
            return last_pos
        last_pos = pos



print find_last('aaaa', 'a')
print find_last('aaaaa', 'aa')
print find_last('aaaa', 'b')
print find_last("111111111", "1")
print find_last("222222222", "")
print find_last("", "3")
print find_last("", "")