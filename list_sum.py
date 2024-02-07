list=[]
sum=0
print("ENTER THE NUMBER OF ELEMENTS")
n=int(input())
print("ENTER THE ELEMENTS")
for i in range(0,n):
    a=int(input())
    sum=sum+a
    list.append(a)
print(list)   
print("THE SUM IS "+str(sum)) 