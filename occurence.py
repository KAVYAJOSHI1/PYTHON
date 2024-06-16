#change
print("ENTER THE STRING")
a=str(input())
count=0
len=len(a)
for i in range(len):
    count=0
    if a[i] in a:
        count=count+1
    print("COUNT OF "+a[i]+"IS "+str(count))    
