#PYTHON PROGRAM TO MERGE 2 SORTED LIST
print("ENTER THE SIZE FOR LIST 1:")
n=int(input())
print("ENTER THE SIZE FOR LIST 2:")
m=int(input())
list1=[]
list2=[]
print("ENTER THE ELEMENTS FOR LIST 1")
for i in range(0,n):
    list1.append(int(input()))
print(list1)    
print("ENTER THE ELEMENTS FOR LIST 2")
for i in range(0,m):
    list2.append(int(input()))
print(list2)
for i in range (0,m):
    list1.append(list2[i])

list1.sort(reverse=True)
print(list1)
    

