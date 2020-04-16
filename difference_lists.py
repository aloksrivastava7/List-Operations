'''
DIFFERENCE OF TWO LISTS
'''

#PROGRAM

ls1 = eval(input('Enter First List : '))
ls2 = eval(input('Enter Second List : '))
ls = []

for i in range(len(ls1)):
    for j in range(len(ls2)):
        if ls1[i] in ls2 :
            break
        else :
            ls.append(ls1[i])
            break
print('Difference of Both Lists =',ls)  
