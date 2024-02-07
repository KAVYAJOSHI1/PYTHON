a=["1","2","3"]
b=["4","5","6"]
a.extend(b)

print(a)
a.append(7)
print(a)
print("LENGTH IS "+str(len(a)))
a.remove(1)
a.pop(0)