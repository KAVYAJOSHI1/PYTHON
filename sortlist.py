list=[]
print("ENTER THE SIZE ")
n=int(input())
for i in range(n):
    print("ENTER THE VALUE")
    list.append(int(input()))
print("SORTED LIST IN ASCENDING ORDER IS:")
list.sort()
print(list)
print("SORTED LIST IN DESCENDING ORDER IS:")
list.sort(reverse=True)
print(list)