a=[2,4,5,6]
b=[]
for i in a:
    b.append(float(i))
print(b)
#map runs a function on all items in a collection
c=[]
c=tuple(map(complex,a))
d=list(map(lambda x:x*2,a))
print(d)