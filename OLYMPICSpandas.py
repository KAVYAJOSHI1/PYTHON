#EXPLORATORY DATA ANALYSIS OF Olympics DATASET USING PANDAS
import pandas as pd
data=pd.read_csv("C:/Users/KAVYA JOSHI/Downloads/archive/athlete_events.csv")
print(data.head(2))
print(data["Year"].min())#TO FIND THE MINIMUM VALUE 
seasons=(data["Year"].unique())#TO COUNT THE UNIQUE VALUES
seasons.sort()
print(len(seasons))#TO COUNT THE UNIQUE VALUES
print(data.duplicated().sum())
#print column
print(data.columns)
#COUNTRY WITH MOST NUMBER OF MEDALS
print(data.groupby("Team")["Medal"].count().sort_values(ascending=False).head(10))

#AVERAGE WEIGHT ,AGE,HEIGHT OF THE ATHLETES BY GENDER AND SPORT
print(data.groupby(by=["Sex","Sport"])[["Height","Weight","Age"]].mean().reset_index())
avg_age_h_w=(data.groupby(by=["Sex","Sport"])[["Height","Weight","Age"]].mean())
a=(avg_age_h_w["Sex"]=="F")
print(a)