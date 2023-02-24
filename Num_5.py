# num 5

list = [1, 2, 3, 4, 5, 4, 2, 3,7]

def newlist(list):
    mynewlist = []
    for num in list:
        if num not in mynewlist:
            mynewlist.append(num)
            return mynewlist
uniquelist = newlist(list)
print(uniquelist)

