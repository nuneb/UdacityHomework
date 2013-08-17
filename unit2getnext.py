#!/usr/bin/env python

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', (start_quote +1))
    url = page[start_quote+1:end_quote]
    return url, end_quote

url, endpos = get_next_target('Here is a <a href="http://udacity.com">link:')
if url:
    print "Here!"
else:
    print "Not here!"

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            pae = page[endpos:]
        else:
            break

