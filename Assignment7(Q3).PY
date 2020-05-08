'''

A fixed point in an array is an element whose value is equal to its index . Given a sorted
array of distinct elements , return a fixed point , if one exists .Otherwise , return False .

For Example , given [-6,0,2,40] , you should return 2 .Given [1,5,7,8] , you should return 2 .
Given [1,5,7,8] , you should return False .

'''

#PROGRAM

ls = eval(input('Enter the List : '))
result = False
for i in range(0,len(ls)):
    if ls[i] == i:
        val = i
        result = True
        break
if result == True:
    print(val)
else :
    print('False')
