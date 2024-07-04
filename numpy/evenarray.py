import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
b=a%2==0
new_a=a[b]
print(new_a)