#!/usr/bin/env python

def fix_machine(debris, product):
    if debris.find(product):
        return product
    else:
        return 'Test Case Sucks'
        
### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') #== "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') #== 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') #== 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') #== 't-shirt'
