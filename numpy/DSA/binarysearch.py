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
f=0
l=n-1
print("ENTER THE NUMBER TO BE SEARCHED:")
x=int(input())
temp=0
while(f<=l):
    mid=int((f+l)/2)
    if list[mid]==x:
        temp=1
        print("THE NUMBER FOUND AT INDEX "+str(mid+1))
        break
    elif list[mid]<x:
        f=mid+1
    else:
        l=mid-1
if temp==0:
    print("THE NUMBER NOT FOUND")    