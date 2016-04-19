# orgonizing data structure

index = []

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']],
#>>> ['computing', ['http://acm.org']]]

# lookup for list with keyword
index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    for e in index:
        if e[0] == keyword:
            return e[1]
    return []

print lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']

# add splitted content to the index list
index = []

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)

add_page_to_index(index,'fake.text',"This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]
