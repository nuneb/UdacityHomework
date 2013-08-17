#!/usr/bin/env python

def weekend(day):
    if day == 'Sunday':
        return True
    if day == 'Saturday':
        return True
    else:
        return False
    
print weekend('Monday')
print weekend('Saturday')
print weekend('July')