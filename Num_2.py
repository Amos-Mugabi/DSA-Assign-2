# Num 2
mylist = [2, 3, 4, 5, 6, 7, 8, 1]
def sumofeven(mylist):
    
    evennum = 0
    for num in mylist:
        if num % 2 == 0:
            evennum += num
    return evennum


even_sum = sumofeven(mylist)s
print(even_sum)
