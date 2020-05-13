'''

You are given three integers X,Y,Z representing the dimensions of a cuboid along with an integer N.
You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of
i+j+k is not equal to N. Here [0 <= i <= X,0 <= j <= Y,0 <= k <= z]
Sample Input 0

1
1
1
2

Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


'''

#PROGRAM

x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if ((i+j+k)!=n) ])
