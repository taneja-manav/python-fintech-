import pandas as pd
import numpy as np

df = pd.read_csv("Uncleaned.csv")
# print(df.head(10))
# print(df.info())
# print(df.describe())
# print(df.shape)
# missing_values =df.isnull().sum()
# print(missing_values)
# df["salary"] = pd.to_numeric(df["salary"])
df["Salary"] = df["Salary"].replace("Sixty Thousand",60000)
df["Salary"] = pd.to_numeric(df["Salary"])
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df.loc[(df["Age"]<18)|(df["Age"]>60),"Age"]=np.nan
df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Gender"].value_counts()


valid_Genders=["Male","Female"]
df["Gender"] = df["Gender"].apply(lambda x: x if x in valid_Genders else "Others")

df["Department"].value_counts()
df["Department"] = df["Department"].replace("Sales&Marketing","Sales")
df["Department"] = df["Department"].replace("Manegement","Management")
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])

df["Hire Date"] = pd.to_datetime(df["Hire Date"],errors="coerce").fillna("Invalid Date")

# missing_values =df.isnull().sum()
# print(missing_values)  
# print(df.info())
df.to_csv("cleaned.csv",index=False)




