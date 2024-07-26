import numpy as np
print("ENTER THE SIZE OF THE ARRAY:")
n=int(input())
list=[]
print("ENTER THE ARRAY ELEMENTS :")
for i in range(n):
    list.append(int(input()))
a=np.array(list)
print("THE ARRAY BEFORE SORTING IS:")
print(a)
min=0
temp=0
for i in range (0,n):
    for j in range(i+1,n):
        min=a[i]
        if(a[j]<min):
            min=a[j]
            temp=a[i]
            a[i]=a[j]
            a[j]=temp

print("THE SORTED ARRAY IS:")
print(a)
