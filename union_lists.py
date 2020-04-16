'''
UNION OF TWO LISTS
'''

#PROGRAM

ls1 = eval(input('Enter First List : '))
ls2 = eval(input('Enter Second List : '))
ls = []

for i in range(len(ls1)):
    ls.append(ls1[i])
for j in range(len(ls2)):
    if ls2[j] in ls :
        continue
    else :
        ls.append(ls2[j])
print('Union of Both Lists =',ls)    
