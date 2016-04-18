# check is column equal to row?
def symmetric(myList):
    # Your code here
    length = len(myList)
    if length == 0:
        return True
    len2 = len(myList[0])
    if(len2!=length):
        return False
    i = 0
    while i<length:
        x = 0
        while x < length:
            if myList[i][x] != myList[x][i]:
                return False
            x+=1
        i+=1
    return True


print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False
