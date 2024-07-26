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
    min=a[n-1]
    pos=n-1
    for j in range(i+1,n):
        if a[j]<min:
            min=a[j]
            pos=j

    if(i<=pos):
        temp=a[i]
        a[i]=a[pos]
        a[pos]=temp
       
        

print("THE SORTED ARRAY IS:")
print(a)
