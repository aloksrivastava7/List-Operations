'''
SYMMETRIC DIFFERENCE OF TWO LISTS
'''

#PROGRAM

ls1 = eval(input('Enter First List : '))
ls2 = eval(input('Enter Second List : '))
ls = []
for i in range(len(ls1)):
    for j in range(len(ls2)):
        if ls1[i] not in ls2:
            ls.append(ls1[i])
            break
for j in range(len(ls2)):
    if ls2[j] not in ls1:
        ls.append(ls2[j])
print('Symmetric Difference of Both Lists =',ls)  

