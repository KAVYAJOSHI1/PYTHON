import pandas as pd
import seaborn as sns
import matplotlib as plt
data=pd.read_csv("pandas1.csv")
#Basic inspection
print(data)
print(data.columns)
print(data.head())
print(data.describe())

#Filtering data
print(data[data["Department"]=="Engineering"])
print(data[data["Salary"]>60000])

#Aggregation and grouping
print(data.groupby("Department")["Salary"].mean())
print(data.groupby("Department")["Salary"].max().idxmax())
print(data.groupby("Department")["Age"].mean().idxmax())

#Data Manipulation
data["Bonus"]=data["Salary"]*0.1
print(data)
new_data=data[(data["Age"]>30) & (data["Salary"]<80000)]
print(new_data)

#Sorting data
#data.sort_values(by="Age",ascending=True)
a=data.sort_values(by="Salary",ascending=False)
print(a)

#Handling missing data
x=data["Age"].mean()
data["Age"].fillna(x,inplace=True)
print(data)
print(data.isnull().sum())
data.loc["John"]=None
data.dropna(subset=["Age"],inplace=True)
print(data)

#Advanced Operations
print(data[data["Salary"]==data["Salary"].max()])
print(data["Salary"].sum())

