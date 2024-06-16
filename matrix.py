print("ENTER THE SIZE")
list=[]
n=int(input())
print("ENTER THE ELEMENT")
for i in range(0,n):
    row=[]
    for j in range(0,n):
        row.append(int(input()))
    list.append(row)
print("THE MATRIX IS:")
for i in range(0,n):
    for j in range(0,n):
        print(list[i][j] ,end=" ")
    print()