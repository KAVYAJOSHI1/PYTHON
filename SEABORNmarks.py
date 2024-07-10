import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
price=[6,5,4]
demand=[4,5,6]
df=pd.DataFrame({"demand":demand,"price":price})
print(df)
sns.barplot(x="demand",y="price",data=df)

plt.title("RESULT GRAPH")
plt.show()
print(df.corr())