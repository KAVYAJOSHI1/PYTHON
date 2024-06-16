a=[]
print("ENTER THE SIZE OF THE LIST")
n=int(input())
print("ENTER THE NUMBERS ")
for i in range(n):
    a.append(int(input()))
a=list(map(lambda x:x*x,a))
print(a)