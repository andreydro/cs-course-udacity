# mesure time of execution
import time

def time_execution(code):
  start = time.clock()
  result = eval(code)
  run_time = time.clock() - start
  return result, run_time

def spin_loop(n):
  i = 0
  while i < n:
    i = i + 1

print time_execution('spin_loop(1000)')
print time_execution('spin_loop(10000)')
print time_execution('spin_loop(100000)')
print time_execution('spin_loop(10 ** 5)')
print time_execution('spin_loop(10 ** 6)')

# print out a number representing the bucket for that keyword.

def hash_string(keyword,buckets):
    h = 0
    for e in keyword:
        h = (h + ord(e)) % buckets
    return h

print hash_string('a',12)
#>>> 1

print hash_string('b',12)
#>>> 2

print hash_string('a',13)
#>>> 6

print hash_string('au',12)
#>>> 10

print hash_string('udacity',12)
#>>> 11

# add any number of empty buckets to the bucket
def make_hashtable(nbuckets):
    h = 0
    table = []
    while h < nbuckets:
        table.append([])
        h = h + 1
    return table

print make_hashtable(3)

# the same procedure, but shorter and with "range"
def make_hashtable(nbuckets):
  table = []
  for unused in range(0,nbuckets):
    table.append([])
  return table

# stuff with buckets
def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]


def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table


table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

print hashtable_get_bucket(table, "Zoe")
#>>> [['Bill', 17], ['Zoe', 14]]

print hashtable_get_bucket(table, "Brick")
#>>> []

print hashtable_get_bucket(table, "Lilith")
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]

# + one more feature (add)

def hashtable_add(htable, key, value):
  hashtable_get_bucket(htable, key).append([key, value])

# + one more feature (lookup)

def hashtable_lookup(htable, key):
  bucket = hashtable_get_bucket(htable, key)
  for entry in bucket:
    if entry[0] == key:
      return entry[1]
  return None

# + one more feature (update)

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return htable
    bucket.append([key, value])
    return htable

# define dictionary
    population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}

print population['Mumbai']

#

def lookup(index, keyword):
  if keyword in index:
    return index[keyword]
  return None
