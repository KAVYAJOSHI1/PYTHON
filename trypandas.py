import pandas as pd

"""data=pd.read_csv("C:/Users/KAVYA JOSHI/Downloads/DATASETS/TITANIC.csv")
print(data.to_string())"""

#dataframe from dictionary

"""data={
    "a":["A","B","C"],
    "n":[1,2,3],
}

df=pd.DataFrame(data)
print(df)
#pandas version
print(pd.__version__)"""

#series FROM LIST

a={"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]}
b=pd.DataFrame(a,index=["r1","r2","r3"])
print(b)


