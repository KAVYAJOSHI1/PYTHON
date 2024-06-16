import pandas as pd 
data=pd.read_csv("C:/Users/KAVYA JOSHI/Downloads/archive/netflix.csv")
#print(data)
#print(type(data))
#print(data.head(7))
#print(data.tail(5))
#print(data.info())
#print(data.describe())
#print(data.shape)
#print(data.index)
#print(data.columns)
#print(data.dtypes)
#print(data.Date)
#print(data[['Date', 'Global Revenue']])
#print(data["Global Revenue"].max())#sum,min,mean,median
#print(data["Global Revenue"].unique())
#print(data["APAC  ARPU"].value_counts())#TO COUNT THE NUMBER OF OCCURENCE

"""TO INSERT NEW COLUMN
data["EMEA  Members*10"]=data["EMEA  Members"]*10
print(data)
"""


"""#data.drop("Date",axis=1,inplace=True)#TO DELETE THE COLUMN PERMENENTLY#0 for row and 1 for column
data.drop([5],axis=0,inplace=True)
print(data)"""

#LOCATE DATA
#print(data["Date"][5:8])
#print(data.loc[1:3,["Date","Global Revenue"]])
#print(data.iloc[1]) #ACTUAL INDEX IS KEPT IN MIND
#GROUP BY
#print(data.groupby("Date")["Global Revenue"].sum())

#TO SEARCH FOR PARTICULAR CONDITION
#print(data[data["Date"].str.contains("2022")].value_counts())