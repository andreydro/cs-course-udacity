# pick one example
def pick_one(a,b,c):
    if a == True:
        return b
    else:
        return c



print pick_one(True, 37, 'hello')
#>>> 37

print pick_one(False, 37, 'hello')
#>>> hello

print pick_one(True, 'red pill', 'blue pill')
#>>> red pill

print pick_one(False, 'sunny', 'rainy')
#>>> rainy
