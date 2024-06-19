#EXPLORATORY DATA ANALYSIS OF Olympics DATASET USING PANDAS
import pandas as pd
data=pd.read_csv("C:/Users/KAVYA JOSHI/Downloads/DATASETS/athlete_events.csv")
#print(data.head(2))
#print(data["Year"].min())#TO FIND THE MINIMUM VALUE 
#seasons=(data["Year"].unique())#TO COUNT THE UNIQUE VALUES
#seasons.sort()
#print(len(seasons))#TO COUNT THE UNIQUE VALUES
#print(data.duplicated().sum())
#print column
#print(data.columns)
#COUNTRY WITH MOST NUMBER OF MEDALS
#print(data.groupby("Team")["Medal"].count().sort_values(ascending=False).head(10))

#AVERAGE WEIGHT ,AGE,HEIGHT OF THE ATHLETES BY GENDER AND SPORT
#print(data.groupby(by=["Sex","Sport"])[["Height","Weight","Age"]].mean().reset_index())
#a=(data.groupby(by=["Sex","Sport"])[["Height","Weight","Age"]].mean().reset_index())
#print(a[(a['Sex']=='F')].query('Sport=="Cycling"'))

#AVERAGE AGE OF THE ATLETE CHANGED OVER THE  YEARS FOR EACH SPORT
a=(data.groupby(by=["Sport","Year"])["Age"].mean().reset_index())#.query('Sport ==" Archery"'))

print(a.query('Sport == "Archery"'))
#TO FIND THE ATHELETES WHO HAVE PARRTICIPATED MULTIPLE TIMES IN THE OLYMPICS
"""participation=data.groupby(by="Name").filter(lambda x:x['Year'].nunique()>1)
print(participation)
participation[["Name","Year","Sport"]].drop_duplicates()"""

#MOST COMMON HEIGHT AND WEIGHT OF MEDAL WINNERS
#print(data[data.Medal.notna()][['Height','Weight']].mode())

#NUMBER OF PARTICIPATING ATHLETES EVOLVED OVER THE YEARS

#print(data.groupby(by="Year")["ID"].nunique().reset_index())

#WHICH SPORT HAS SEEN SIGNIFICANT INCREASE OR DECREASEIN PARTICIPATION OVER THE YEARS

"""a=(data.groupby(by=["Sport","ID"])["Name"].nunique().reset_index())
a['change%']=a.groupby('Sport')['ID'].pct_change()
print(a)"""

#GENDER DISTRIBUTION OF THE ATHLETES OVER THE YEAR
#print(data.groupby(by=["Year","Sex","Sport"])["ID"].value_counts())

#WHICH COUNTYR HAS WON MORE MEDALS BASED ON SPORT
#print(data.groupby(by=['NOC','Sport'])['Medal'].count())
#WHTA ARE TRENDS IN MEDAL COUNTS FOR TOP PERFORMINGCOUNTRIES OVER THE YEARS

#print(data.groupby(by=['Year','NOC'])['Medal'].count().sort_values(ascending=False).head(10))
