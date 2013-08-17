#!/usr/bin/env python

print 7 * 7 * 24 * 60

speed_of_light = 299792458   # meters per second
centimeters = 100            # one meter is 100 centimeters
nanosecond = 1.0/1000000000  # one billionth of a second

print speed_of_light * centimeters * nanosecond

speed_of_light = 299792458.0 # meters per second
cycles_per_second = 2700000000.0 #2.7 GHz

cycle_distance = speed_of_light / cycles_per_second
print cycle_distance

age = 32
days = 365.25
print age * days

s = 'Nune'
t = 'n'
i = 2

s = 'audacity'
print 'U' + s[2:]

print s.find(t,i)
print s[i:].find(t)
print s[i:].find(t) + i
print s[i:].find(t[i:])

