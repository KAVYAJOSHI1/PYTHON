#array program to insert ,delete ,reverse array,search for an element
import numpy as np
a=np.array([1,2,3,4,5])
print("original array:\n")
print(a)
a=np.insert(a,5,6)
print("inserted array:\n")
print(a)
a=np.delete(a,2)
print("deleted array:\n")
print(a)
a=a[::-1]
print("reversed array:\n")
print(a)
print("ENTER THE ELEMENT TO BE SEARCHED:\n")
x=int(input())
if x in a:
    INDEX=np.where(a==x)[0]+1
    print("ELEMENT FOUND AT POSITION"+ str(INDEX))
else:
    print("ELEMENT NOT FOUND")

