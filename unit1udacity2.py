#!/usr/bin/env python
speed_of_light = 299800000. # meters per second
nano_per_sec = 1000000000. # 1 billion
nanosecond = 1.0/nano_per_sec

nanodistance = speed_of_light * nanosecond

print nanodistance



text = "all zip files are zipped" 

first_zip = text.find('zip')
second_zip = text.find('zip', (first_zip +1))

print second_zip

x = 3.14159
y = x + .5  # creates new variable y, x + .5. Adding .5 is key.
z = str(y)   # a string encoded version of y, new variable z
place = z.find('.') # finds decimal point

print z[0 : place ] # prints the number from position 0 up until the decimal

s = 'CidatyUcityda'
print s[6] + s[-2:] + s[7:12]
print s[6] + s[-2:] + s[7:11]
print s[6] + s[2:4] + s[7:13]
print s[-7] + s[2:4] +s[7:11]
print s[6] + s[-2] + s[3] + s[-2] + s[4:6]
print s[6] + s[2] + s[3] + s[7:11]

n = 'NuneGreg'
print n[-2:]