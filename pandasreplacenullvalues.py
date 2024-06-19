import pandas as pd
import numpy as np
pd.options.display.max_columns=10
pd.options.display.max_rows=500
data=pd.read_csv("C:/Users/KAVYA JOSHI/Downloads/DATASETS/TITANIC.csv")
#print number of null in particular column
print
data["Age"].fillna(54,inplace=True)
print(data.isnull().sum())
print(data["Age"])