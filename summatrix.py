print("ENTER THE SIZE OF THE MATRIX\n")
n=int(input())
matrixA=[]
print("ENTER THE ELEMENTS OF MATRIX A")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(input("ENTER ELEMENT"+str(i)+","+str(j)+"\n"))
    matrixA.append(row)
matrixB=[]
print("ENTER THE ELEMENTS OF MATRIX A")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(input("ENTER ELEMENT"+str(i)+","+str(j)+"\n"))
    matrixB.append(row)

print("THE SUM OF MATRIX IS:\n")
sum=[]
for i in range(n):
    for j in range(n):
        sum=matrixA[i][j]+matrixB[i][j]
        print(sum)
    
    
