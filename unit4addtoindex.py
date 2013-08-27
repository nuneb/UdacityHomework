#!/usr/bin/env python
# Define a procedure, add_to_index,
# that takes 3 inputs:
# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []
def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    return index.append([keyword,[url]])


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]


def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return[]

print lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']    

def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)

add_page_to_index(index,'fake.text',"This is a test")
print index
    


