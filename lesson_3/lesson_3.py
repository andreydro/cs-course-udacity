# days in a Month
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
def how_many_days(month_number):
    return days_in_month[month_number - 1]

print how_many_days(1)
#>>> 31

print how_many_days(9)
#>>> 30

# print out Delhi
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

print countries[1][1]

# Multiple of China and Romania population
print countries[0][2] / countries[2][2]

# change Curly to Shemp
stooges = ['Moe','Larry','Curly']

stooges[2] = 'Shemp'
print stooges

# sum 3 elemets of list
def sum_list(l):
    return l[0] + l[1] + l[2]

print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134

# print out number of elements which starts from "U"
def measure_udacity(p):
    result = 0
    for i in p:
        if i[0] == "U":
            result = result + 1
    return result

print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2

# print out index of element that equal to the value
def find_element(p,v):
    i = 0
    for e in p:
        if e == v:
            return i
        i = i + 1
    return - 1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

# -//- v.2
def find_element(p,t):
    for e in p:
        if e == t:
            return p.index(e)
    return -1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
