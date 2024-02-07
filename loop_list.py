a=[1,2,3,4]
for i in a:
    print(i)
for i in range(0,3):
    for j in range(0,3):
        print(a[i])
a.sort(reverse=True)
print(a)        