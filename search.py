list=[]
print("ENTET THE SIZE")
n=int(input())
print("ENTER THE ARRAY ELEMENTS")
for i in range(n):
    list.append(int(input()))
print("ENTER THE ELEMENT TO BE SEARCHED")
x=int(input())
if x in list:
    print("ELEMENT FOUND")
else:
    print("ELEMENT NOT FOUND")
