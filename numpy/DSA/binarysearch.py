import numpy as np
print("ENTER THE SIZE OF THE ARRAY:")
n=int(input())
list=[]
print("ENTER THE ELEMENTS:")
for i in range(n):
    list.append(int(input()))
a=np.array(list)
for i in range(n-1):
    for j in range(i+1,n):
        if(list[i]>list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print("THE SORTED ARRAY IS:")            
print(list)
    