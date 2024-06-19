import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
roll_no=[1,2,3,4,5,6,7,8,9]
marks=[70,80,90,100,70,20,30,40,50]
df=pd.DataFrame({"Roll_no":roll_no,"Marks":marks})
print(df)
sns.barplot(x="Roll_no",y="Marks",data=df)

plt.title("RESULT GRAPH")
plt.show()