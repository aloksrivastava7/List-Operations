'''
INTERSECTION OF TWO LISTS
'''

#PROGRAM

ls1 = eval(input('Enter First List : '))
ls2 = eval(input('Enter Second List : '))
ls = []
for i in range(len(ls1)):
    for j in range(len(ls2)):
        if ls2[j]==ls1[i]:
            ls.append(ls1[i])
print('Intersection of Both Lists =',ls)    
