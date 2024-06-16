a=["apple","banana","orange","mango"]
b=[]
for i in a:
    if "p" in i:
        b.append(i)
print(b) 
#comprehend list
c=[i for i in a if i!="mango"] 
print(c)      