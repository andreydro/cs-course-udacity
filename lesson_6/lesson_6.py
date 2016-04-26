# define factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print factorial(0)
#>>> 1

print factorial(5)
#>>> 120

print factorial(10)
#>>> 3628800

# define palindrome
def is_palindrome(s):
    if s == '':
        return True
    elif s[0] == s[-1] and s[1] == s[-2]:
        return True
    else:
        return False

print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True

#define fibonacci numbres with recursive definition
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print fibonacci(0)
#>>> 0
print fibonacci(1)
#>>> 1
print fibonacci(15)
#>>> 610

# define fibonacci numbers with a loop
def fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

# define compute_ranks

def compute_ranks(graph):
  d = 0.8 # damping factor
  numloops = 10

  ranks = {}
  npages = len(graph)
  for page in graph:
    ranks[page] = 1.0 / npages

  for i in range(0, numloops):
    newranks = {}
    for page in graph:
      newrank = (1 - d) / npages
      #
      for node in graph:
        if page in graph[node]:
          newrank = newrank + d * (ranks[node] / len(graph[node]))
      newranks[page] = newrank
    ranks = newranks
  return ranks

print fibonacci(36)
#>>> 14930352

# rabbits die after 6 months
def rabbits(n):
    if n < 1:
        return 0
    else:
        if n == 1 or n == 2:
            return 1
        else:
            return rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)

print rabbits(10)
#>>> 35

# Spreading
def hexes_to_udaciousness(n, spread, target):
    if n >= target:
        return 0
    else:
        return 1 + hexes_to_udaciousness(n * (1 + spread), spread, target)

# 0 more needed, since n already exceeds target
print hexes_to_udaciousness(100000, 2, 36230)
#>>> 0

# after 1 hexamester, there will be 50000 + (50000 * 2) Udacians
print hexes_to_udaciousness(50000, 2, 150000)
#>>> 1

# need to match or exceed the target
print hexes_to_udaciousness(50000, 2, 150001)
#>>> 2

# only 12 hexamesters (2 years) to world domination!
print hexes_to_udaciousness(20000, 2, 7 * 10 ** 9)
#>>> 12

# more friends means faster world domination!
print hexes_to_udaciousness(15000, 3, 7 * 10 ** 9)
#>>> 10

# deep count
def is_list(p):
    return isinstance(p, list)

def deep_count(p):
    sum = 0
    for e in p:
        sum = sum + 1
        if is_list(e):
            sum = sum + deep_count(e)
    return sum

print deep_count([1, 2, 3])
#>>> 3

# The empty list still counts as an element of the outer list
print deep_count([1, [], 3])
#>>> 3

print deep_count([1, [1, 2, [3, 4]]])
#>>> 7

print deep_count([[[[[[[[1, 2, 3]]]]]]]])
#>>> 10

# feeling lucky
def lucky_search(index, ranks, keyword):
  pages = lookup(index, keyword)
  if not pages:
    return None
  best_page = pages[0]
  for candidate in pages:
    if ranks[candidate] > ranks[best_page]:
      best_page = candidate
  return best_page
