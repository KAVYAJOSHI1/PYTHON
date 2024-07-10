from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(random.normal(loc=2,scale=1,size=(3,3)),kde=False)
plt.show()