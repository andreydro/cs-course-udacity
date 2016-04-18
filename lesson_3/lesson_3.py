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

#multiply all elements of list
def product_list(list_of_numbers):
    result = 1
    if len(list_of_numbers) >= 1:
        for e in list_of_numbers:
            result *= e
        return result
    else:
        return 1

print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1

# print out greatest number of list
def greatest(list_of_numbers):
    num = 0
    for e in list_of_numbers:
        if e > num:
            num = e
    return num

print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

#print out number of sudents and total tuition
udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(p):
    t_students = 0
    t_tuition = 0
    for uni, students, price in p:
        t_students = t_students + students
        t_tuition = t_tuition + students * price
    return t_students, t_tuition

print total_enrollment(udacious_univs)
#>>> (90000,0)

print total_enrollment(usa_univs)
#>>> (77285,3058581079)

# diffirence between adding and appending
list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5, 6]
list2.append([5, 6])

print "showing list1 and list2:"
print list1
print list2
