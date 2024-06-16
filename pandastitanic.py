#FILTERING TITANIC DATASET
import pandas as pd
data=pd.read_csv("C:/Users/KAVYA JOSHI/Downloads/DATASETS/TITANIC.csv")
#print(data.isnull())#TO CHECK THE NULL VALUES
#print(data.isnull().sum())#TO COUNT THE NULL VALUES
#print(data["Age"].fillna(data["Age"].mean().round(),inplace=True))#TO FILL THE NULL VALUES
#print(data.shape)
#data.dropna(axis=0,inplace=True)
#data.drop('Cabin',axis=1, inplace=True)
#print(data.duplicated().sum())#TO COUNT THE DUPLICATE VALUES
#data.drop_duplicates()#TO REMOVE THE DUPLICATE VALUES
print(data)
