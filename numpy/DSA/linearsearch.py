#Linear search
import numpy as np
print("Enter the size of array")
n=int(input())
LIST=[]
print("ENTER THE ELEMENTS")
for i in range(n):
    LIST.append(int(input()))
a=np.array(LIST) 
print("ENTER THE NUMBER TO BE SEARCHED")
x=int(input())
for i in range(n):
    if(a[i]==x):
        print("THE NUMBER FOUND AT POSITION "+str(i+1))
        break
    else:
        print("THE NUMBER NOT FOUND")   

