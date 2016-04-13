# sum and square
def sum(a,b):
  c = a + b
  return c

def square(x):
  x = x * x
  return x

print square(5)

# sum of 3
def sum(a,b):
  return a + b

def sum3(a,b,c):
  return a + b + c

print sum3(1,2,3)

print sum3(93,53,70)

# strange output
def abbaize(a,b):
  return a + b + b + a

print abbaize('a','b')
#>>> 'abba'

print abbaize('dog','cat')
#>>> 'dogcatcatdog'

# procesdure find second argument in string
def find_second(var, word):
  return var.find(word,(var.find(word) + 1))

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')
#>>> 25

twister = "she sells seashells by the seashore"
print find_second(twister,'she')
#>>> 13

# bigger number
def bigger(x,y):
  if x > y:
    return x

    return y

print bigger(2,7)
#>>> 7

print bigger(3,2)
#>>> 3

print bigger(3,3)
#>>> 3

# Who`s name start from D is a friend
def is_friend(a):
  if a[0] == "D":
    return True
  else:
    return False

print is_friend('Diane')
#>>> True

print is_friend('Fred')
#>>> False

# Who`s name start  from D or N is a friend
def is_friend(name):
  if name[0] == "D" or name[0] == "N":
    return True
  else:
    return False

print is_friend('Diane')
#>>> True

print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False

# biggest number
def biggest(a, b, c):
  if a >= b and a >= c:
    return a
  if b >= c and b >= a:
    return b
  if c >= a and c >= b:
    return c

print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9

# print numbers
def print_numbers(n):
  x = 1
  while x <= n:
    print x
    x = x + 1

print_numbers(3)
#>>> 1
#>>> 2
#>>> 3

# factorial
def factorial(n):
  x = 1
  while n >= 1:
    x = x * n
    n = n - 1
  return x

print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720

# find link with posibility "No links"
def get_next_target(page):
  start_link = page.find('<a href=')
  if start_link == -1:
    return None, 0

  start_quote = page.find('"', start_link)
  end_quote = page.find('"', start_quote + 1)
  url = page[start_quote + 1:end_quote]
  return url, end_quote

# print out "Udacians"
def udacify(arg):
  return "U" + arg

print udacify('dacians')
#>>> Udacians

print udacify('turn')
#>>> Uturn

print udacify('boat')
#>>> Uboat

# median
def bigger(a,b):
  if a > b:
    return a
  else:
    return b

def biggest(a,b,c):
  return bigger(a,bigger(b,c))

def median(a,b,c):
  big = biggest(a,b,c)
  if big == a:
    return bigger(b,c)
  if big == b:
    return bigger(a,c)
  else:
    return bigger(a,b)

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7

# print numbers + "Blastoff!"
def countdown(n):
  while n != 0:
    print n
    n = n - 1
    if n == 0:
        print "Blastoff!"
        break

countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!

