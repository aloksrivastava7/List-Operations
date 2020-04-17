'''

SAMPLE INPUT : Enter a List : [10,0,20,0,30,0,40]

SAMPLE OUTPUT : Resultant List :  [10, 20, 30, 40, 0, 0, 0]

That is , we have to create a program to shift all the zeroes of the List at the Last

'''

#PROGRAM

ls = eval(input('Enter a List : '))
l = len(ls)
for i in range(0,l):
    if ls[i] == 0:
        del ls[i]
        ls.append(0)
print('Resultant List : ',ls)        
