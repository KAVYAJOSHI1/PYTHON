import pandas as pd
pd.options.display.max_rows=500
data=pd.read_csv("C:/Users/KAVYA JOSHI/Downloads/DATASETS/TITANIC.csv")
#REMOVE NULL ROWS
data.dropna(inplace=True)
print(data)
