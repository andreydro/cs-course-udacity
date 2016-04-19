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

# split the string with choosen characters
def split_string(source,splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                output[-1] = output[-1] + char
    return output

# time spent at routers
total_time = 75
one_way_distance = 2500.0
optic_speed = 200000
ms_per_second = 1000

# calculations
time_on_the_wires = 2 * one_way_distance / optic_speed * ms_per_second

total_time_at_routers = total_time - time_on_the_wires
print total_time_at_routers
