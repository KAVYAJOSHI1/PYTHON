#A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
#[[3,7,8],[9,11,13],[15,16,17]]
import numpy as np
print("ENTER THE ROW SIZE AND COLUMN SIZE")
n=int(input())
m=int(input())
print("ENTER THE MATRIX ELEMENTS")

a=np.array([[int(input()) for i in range(n)]for j in range(m)])
print("THE MATRIX IS")
print(a)
for i in range(n):
    for j in range(m):
        if(a[i][j]==min(a[i]) and a[i][j]==max(a[:,j])):
            print("LUCKY NUMBER IS: " ,a[i][j])
            break
      
        

