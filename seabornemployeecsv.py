import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
pd.options.display.max_columns=9
pd.options.display.max_rows=1499
a=pd.read_csv("C:/Users/KAVYA JOSHI/Downloads/DATASETS/hr_data.csv")
print(a.columns)
plt.figure(figsize=(10,5))
#sns.lineplot(x="number_project",y="average_montly_hours",data=a,hue="department",style="left",legend="full",palette="inferno")
#plt.title("RESULT GRAPH")
#plt.show()
sns.histplot(a["average_montly_hours"],kde=False)
plt.show()
