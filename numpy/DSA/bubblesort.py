#Bubble sort
import numpy as np
print("ENTER THE SIZE OF THE ARRAY:")
n=int(input())
list=[]
print("ENTER THE ELEMENTS:")
for i in range(0,n):
    #using numpy
    list.append(int(input()))
a=np.array(list)
print("THE ARRAY IS:")
print(a)
for i in range(0,n-1):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("THE SORTED ARRAY IS:")            
print(a)            

