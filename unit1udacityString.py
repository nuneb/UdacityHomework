#!/usr/bin/env python

s =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

def get_next_target(s):
    start_link = s.find('<a href=')
    start_quote = s.find('"', start_link)
    end_quote = s.find('"', (start_quote +1))
    url = s[start_quote+1:end_quote]
    return url, end_quote

def rest_of_string(s):
    return s[1:]

print url
s = s[end_quote:]
# and then we can repeat from start_link
# or we can do procedural abstraction