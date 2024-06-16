list=[]
print("ENTER THE SIZE")
n=int(input())
print("ENTER THE STRING")
for i in range(n):
 list.append(str(input()))
new_list=[a.strip().capitalize() for a in list]


for a in new_list:
 
 print(a)