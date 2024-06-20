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
