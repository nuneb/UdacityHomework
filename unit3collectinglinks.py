#!/usr/bin/env python

# collecting links
# this does not work as is

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote +1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            return links.append(url)
        else:
            break
    return links

links = get_all_links(get_page('http://www.udacity.com/cs101x/index.html'))

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
# Depth-First Search
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled


