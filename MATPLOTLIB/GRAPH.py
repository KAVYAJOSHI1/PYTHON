import matplotlib.pyplot as plt
import numpy as np
x_axis=np.array([1,2,3,4,5,6,7,9,10])
y_axis=np.array([20,40,60,80,100,120,140,160,180,200])
plt.plot(x_axis,y_axis,marker='o')
plt.title("LINE GRAPH")
plt.xlabel("labour")
plt.ylabel("production")
plt.grid()
plt.show()

