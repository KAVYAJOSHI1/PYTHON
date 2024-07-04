#PROGRAM TO FIND ELEMENTS GREATER THAN 5 
import numpy as np
a=np.array([1,2,40,6,7,2])
filter=[]
for i in a:
    if i>5:
        filter.append(True)
    else:
        filter.append(False)
new_array=a[filter]  
print(new_array)      