#Program to perform insertion sort
import numpy as np
print("ENTER THE SIZE OF THE ARRAY:")
n=int(input())
list=[]
print("ENTER THE ARRAY ELEMENTS TO BE SORTED:")
for i in range(n):
     list.append(int(input()))
a=np.array(list)
print("THE ARRAY BEFORE SORTING IS:")
print(a)  
print("ARRAY AFTER INSERTION SORTING IS:")
for i in range(1,n):
     j=i-1
     temp=a[i]
     while(a[j]>temp and j>=0):
          a[j+1]=a[j]
          j-1
     a[j+1]=temp

print(a)          

          