import numpy as np
a=np.array([[1,2],[9,7]])
b=np.array([[8,4],[2,3]])
c=np.matmul(a, b)
print(c)
print(c[0][1])